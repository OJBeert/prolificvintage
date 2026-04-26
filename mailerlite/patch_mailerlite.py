#!/usr/bin/env python3
"""Patch: replace nl-form with MailerLite embed."""

with open("templates/prolific/index.html", encoding="utf-8") as f:
    html = f.read()

# ── 1. Inject MailerLite style into <head> ────────────────────────────────
ml_style = """<style type="text/css">@import url("https://assets.mlcdn.com/fonts.css?version=1776945");</style>
<style type="text/css">
.ml-form-embedSubmitLoad{display:inline-block;width:20px;height:20px;}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0;}
.ml-form-embedSubmitLoad:after{content:" ";display:block;width:11px;height:11px;margin:1px;border-radius:50%;border:4px solid #fff;border-color:#fff #fff #fff transparent;animation:ml-form-embedSubmitLoad 1.2s linear infinite;}
@keyframes ml-form-embedSubmitLoad{0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}
#mlb2-40421023.ml-form-embedContainer{box-sizing:border-box;display:table;margin:0 auto;position:static;width:100%!important;}
#mlb2-40421023.ml-form-embedContainer h4,#mlb2-40421023.ml-form-embedContainer p,#mlb2-40421023.ml-form-embedContainer span,#mlb2-40421023.ml-form-embedContainer button{text-transform:none!important;letter-spacing:normal!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper{background-color:transparent;border-width:0;border-color:transparent;border-radius:0;border-style:solid;box-sizing:border-box;display:inline-block!important;margin:0;padding:0;position:relative;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper.embedForm{max-width:380px;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-align-center{text-align:center;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody{padding:0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedContent,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent{text-align:center;margin:0 0 16px 0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedContent h4,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent h4{color:#fff;font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:24px;font-weight:400;margin:0 0 8px 0;word-break:break-word;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedContent p,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent p{color:rgba(255,255,255,0.6);font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:13px;font-weight:400;line-height:20px;margin:0;text-align:center;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody form{margin:0;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-formContent{margin:0 0 0 0;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-fieldRow{margin:0 0 10px 0;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-fieldRow.ml-last-item{margin:0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-fieldRow input{background-color:#fff!important;color:#333!important;border-color:#ccc;border-radius:0!important;border-style:solid!important;border-width:1px!important;font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:12px!important;height:auto;line-height:21px!important;margin:0;padding:11px 14px!important;width:100%!important;box-sizing:border-box!important;max-width:100%!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit{margin:8px 0 0 0;float:left;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit button{background-color:#fff!important;border:none!important;border-radius:0!important;box-shadow:none!important;color:#000!important;cursor:pointer;font-family:'Open Sans',Arial,Helvetica,sans-serif!important;font-size:9px!important;font-weight:700!important;letter-spacing:0.22em;text-transform:uppercase;line-height:21px!important;height:auto;padding:11px!important;width:100%!important;box-sizing:border-box!important;transition:opacity 0.2s;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit button.loading{display:none;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit button:hover{opacity:0.8;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent h4{color:#fff!important;}
.ml-error input{border-color:red!important;}
</style>
"""

html = html.replace("</head>", ml_style + "</head>")

# ── 2. Replace nl-form with MailerLite embed div ─────────────────────────
old_form = """  <form class="nl-form" id="nl-form">
    <input class="nl-input" type="email" placeholder="your@email.com" required/>
    <button class="nl-btn" type="submit" data-i18n="nl.btn">登録</button>
  </form>"""

new_form = """  <div id="mlb2-40421023" class="ml-form-embedContainer ml-subscribe-form ml-subscribe-form-40421023">
    <div class="ml-form-align-center">
      <div class="ml-form-embedWrapper embedForm">
        <div class="ml-form-embedBody ml-form-embedBodyDefault row-form">
          <div class="ml-form-embedContent" style="margin-bottom:0;"></div>
          <form class="ml-block-form" action="https://assets.mailerlite.com/jsonp/2293748/forms/185764460472828993/subscribe" data-code="" method="post" target="_blank">
            <div class="ml-form-formContent">
              <div class="ml-form-fieldRow ml-last-item">
                <div class="ml-field-group ml-field-email ml-validate-email ml-validate-required">
                  <input aria-label="email" aria-required="true" type="email" class="form-control" data-inputmask="" name="fields[email]" placeholder="Email" autocomplete="email">
                </div>
              </div>
            </div>
            <input type="hidden" name="ml-submit" value="1">
            <div class="ml-form-embedSubmit">
              <button type="submit" class="primary" data-i18n="nl.btn">登録</button>
              <button disabled="disabled" style="display:none;" type="button" class="loading">
                <div class="ml-form-embedSubmitLoad"></div>
                <span class="sr-only">Loading...</span>
              </button>
            </div>
            <input type="hidden" name="anticsrf" value="true">
          </form>
        </div>
        <div class="ml-form-successBody row-success" style="display:none">
          <div class="ml-form-successContent">
            <h4>Thank you!</h4>
            <p>登録が完了しました。</p>
          </div>
        </div>
      </div>
    </div>
  </div>"""

html = html.replace(old_form, new_form)

# ── 3. Remove old nl-form submit listener ────────────────────────────────
html = html.replace(
    "\ndocument.getElementById('nl-form').addEventListener('submit', e => {\n  e.preventDefault();\n  const msg = document.createElement('p');\n  msg.className = 'nl-success';\n  msg.textContent = '登録しました。';\n  e.target.replaceWith(msg);\n});",
    ""
)

# ── 4. Add MailerLite scripts before </body> ──────────────────────────────
ml_scripts = """
<script>
function ml_webform_success_40421023() {
  var $ = ml_jQuery || jQuery;
  $('.ml-subscribe-form-40421023 .row-success').show();
  $('.ml-subscribe-form-40421023 .row-form').hide();
}
</script>
<script src="https://groot.mailerlite.com/js/w/webforms.min.js?vb397d78ebaa8a0f631d35384c46d781b" type="text/javascript"></script>
<script>fetch("https://assets.mailerlite.com/jsonp/2293748/forms/185764460472828993/takel")</script>
"""

html = html.replace("</body>", ml_scripts + "</body>")

with open("templates/prolific/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✓ MailerLite form patched successfully")
