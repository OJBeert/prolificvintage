#!/usr/bin/env python3
"""Inject Stripe payment links into index.html PRODUCTS array and update JS logic."""

import json, re

with open("stripe_links.json") as f:
    links = {item["id"]: item["link_url"] for item in json.load(f)}

with open("templates/prolific/index.html", encoding="utf-8") as f:
    html = f.read()

# ── 1. Add link + soldOut to each PRODUCTS entry ───────────────────────────
def inject_link(m):
    line = m.group(0)
    id_match = re.search(r'id:(\d+)', line)
    if not id_match:
        return line
    pid = int(id_match.group(1))
    url = links.get(pid, "")
    # Add link and soldOut before the closing }
    return line.rstrip().rstrip("},") + f', link:"{url}", soldOut:false }},'

html = re.sub(r'\{ id:\d+,.*?\},', inject_link, html)

# ── 2. Add SOLD OUT CSS ────────────────────────────────────────────────────
sold_css = """
/* ── SOLD OUT ── */
.sold-badge {
  position: absolute; top: 12px; right: 12px; z-index: 3;
  font-size: 8px; letter-spacing: 0.18em; text-transform: uppercase;
  padding: 4px 10px; font-family: var(--sans);
  background: rgba(12,12,12,0.88); color: #fff;
}
.product-card.sold-out .product-img img { opacity: 0.45; }
.product-card.sold-out .hover-cta { display: none; }
.modal-add.sold { background: var(--gray-2); color: var(--gray-3); cursor: not-allowed; }
"""
html = html.replace("/* ── MODAL ── */", sold_css + "\n/* ── MODAL ── */")

# ── 3. Replace renderGrid card template ───────────────────────────────────
old_grid = """  grid.innerHTML = PRODUCTS.map(p => `
    <div class="product-card" data-id="${p.id}" tabindex="0" role="button" aria-label="${p.name}">
      <div class="product-img">
        <span class="grade-badge${p.grade === 'B' ? ' grade-B' : ''}">Grade ${p.grade}</span>
        <img src="${p.img}" alt="${p.name}" loading="lazy">
        <div class="product-hover">
          <button class="hover-cta" tabindex="-1">詳細を見る</button>
        </div>
      </div>
      <div class="product-info">
        <div class="product-fullname">${p.brand} ${p.name}</div>
        <div class="product-price">${fmt(p.price)}</div>
      </div>
    </div>`).join('');"""

new_grid = """  grid.innerHTML = PRODUCTS.map(p => `
    <div class="product-card${p.soldOut ? ' sold-out' : ''}" data-id="${p.id}" tabindex="0" role="button" aria-label="${p.name}">
      <div class="product-img">
        <span class="grade-badge${p.grade === 'B' ? ' grade-B' : ''}">Grade ${p.grade}</span>
        ${p.soldOut ? '<span class="sold-badge">Sold Out</span>' : ''}
        <img src="${p.img}" alt="${p.name}" loading="lazy">
        <div class="product-hover">
          <button class="hover-cta" tabindex="-1">${p.soldOut ? 'Sold Out' : '詳細を見る'}</button>
        </div>
      </div>
      <div class="product-info">
        <div class="product-fullname">${p.brand} ${p.name}</div>
        <div class="product-price">${p.soldOut ? '<span style="color:var(--gray-3)">SOLD OUT</span>' : fmt(p.price)}</div>
      </div>
    </div>`).join('');"""

html = html.replace(old_grid, new_grid)

# ── 4. Update modal-add button behavior ───────────────────────────────────
old_modal_btn = """  const btn = document.getElementById('modal-add');
  const inCart = cart.some(i => i.id === id);
  btn.textContent = inCart ? 'カート済み' : 'カートに追加';
  btn.classList.toggle('added', inCart);"""

new_modal_btn = """  const btn = document.getElementById('modal-add');
  if (p.soldOut) {
    btn.textContent = 'SOLD OUT';
    btn.className = 'modal-add sold';
    btn.onclick = null;
  } else {
    btn.textContent = '今すぐ購入 →';
    btn.className = 'modal-add';
    btn.onclick = () => window.open(p.link, '_blank');
  }"""

html = html.replace(old_modal_btn, new_modal_btn)

# ── 5. Remove old modal-add click listener (cart logic) ──────────────────
old_listener = """document.getElementById('modal-add').addEventListener('click', () => {
  if (!activeId || cart.some(i => i.id === activeId)) return;
  cart.push(PRODUCTS.find(p => p.id === activeId));
  updateCart();
  document.getElementById('modal-add').textContent = 'カート済み';
  document.getElementById('modal-add').classList.add('added');
  closeModal();
  openCart();
});"""

new_listener = "// modal-add click is set dynamically in openModal()"

html = html.replace(old_listener, new_listener)

# ── 6. Add sold_out.json fetch on page load ───────────────────────────────
old_render = "renderGrid();"
new_render = """// Fetch sold-out list (update sold_out.json via Stripe webhook)
fetch('sold_out.json').then(r => r.json()).then(ids => {
  ids.forEach(id => {
    const p = PRODUCTS.find(x => x.id === id);
    if (p) p.soldOut = true;
  });
}).catch(() => {}).finally(() => renderGrid());"""

html = html.replace(old_render, new_render)

with open("templates/prolific/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✓ index.html updated successfully")
