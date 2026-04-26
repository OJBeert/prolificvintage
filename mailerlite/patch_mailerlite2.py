#!/usr/bin/env python3
"""Patch: update newsletter copy + swap to horizontal MailerLite form."""

with open("templates/prolific/index.html", encoding="utf-8") as f:
    html = f.read()

# ── 1. Replace ML CSS block in <head> ────────────────────────────────────
old_css_block = '''<style type="text/css">@import url("https://assets.mlcdn.com/fonts.css?version=1776945");</style>
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
</style>'''

new_css_block = '''<style type="text/css">@import url("https://assets.mlcdn.com/fonts.css?version=1776945");</style>
<style type="text/css">
.ml-form-embedSubmitLoad{display:inline-block;width:20px;height:20px;}
.g-recaptcha{transform:scale(1);-webkit-transform:scale(1);transform-origin:0 0;-webkit-transform-origin:0 0;}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0;}
.ml-form-embedSubmitLoad:after{content:" ";display:block;width:11px;height:11px;margin:1px;border-radius:50%;border:4px solid #fff;border-color:#ffffff #ffffff #ffffff transparent;animation:ml-form-embedSubmitLoad 1.2s linear infinite;}
@keyframes ml-form-embedSubmitLoad{0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}
#mlb2-40421023.ml-form-embedContainer{box-sizing:border-box;display:table;margin:0 auto;position:static;width:100%!important;}
#mlb2-40421023.ml-form-embedContainer h4,#mlb2-40421023.ml-form-embedContainer p,#mlb2-40421023.ml-form-embedContainer span,#mlb2-40421023.ml-form-embedContainer button{text-transform:none!important;letter-spacing:normal!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper{background-color:transparent;border-width:0px;border-color:transparent;border-radius:0;border-style:solid;box-sizing:border-box;display:inline-block!important;margin:0;padding:0;position:relative;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper.embedForm{max-width:400px;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-align-center{text-align:center;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody{padding:0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody.ml-form-embedBodyHorizontal{padding-bottom:0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedContent,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent{text-align:left;margin:0 0 20px 0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedContent h4,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent h4{color:#ffffff;font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:30px;font-weight:400;margin:0 0 10px 0;text-align:left;word-break:break-word;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedContent p,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent p{color:rgba(255,255,255,0.7);font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:14px;font-weight:400;line-height:20px;margin:0 0 10px 0;text-align:left;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody form{margin:0;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-formContent,#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-checkboxRow{margin:0 0 20px 0;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-checkboxRow{float:left;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-formContent.horozintalForm{margin:0;padding:0 0 20px 0;width:100%;height:auto;float:left;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-fieldRow{margin:0 0 10px 0;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-fieldRow.ml-last-item{margin:0;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-fieldRow input{background-color:#ffffff!important;color:#333333!important;border-color:#cccccc;border-radius:4px!important;border-style:solid!important;border-width:1px!important;font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:14px!important;height:auto;line-height:21px!important;margin:0;padding:10px 10px!important;width:100%!important;box-sizing:border-box!important;max-width:100%!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-horizontalRow{height:auto;width:100%;float:left;}
.ml-form-formContent.horozintalForm .ml-form-horizontalRow .ml-input-horizontal{width:70%;float:left;}
.ml-form-formContent.horozintalForm .ml-form-horizontalRow .ml-button-horizontal{width:30%;float:left;}
.ml-form-formContent.horozintalForm .ml-form-horizontalRow .horizontal-fields{box-sizing:border-box;float:left;padding-right:10px;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-horizontalRow input{background-color:#ffffff;color:#333333;border-color:#cccccc;border-radius:4px;border-style:solid;border-width:1px;font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:14px;line-height:20px;margin:0;padding:10px 10px;width:100%;box-sizing:border-box;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-horizontalRow button{background-color:#ffffff!important;border-color:#ffffff;border-style:solid;border-width:1px;border-radius:4px;box-shadow:none;color:#000000!important;cursor:pointer;font-family:'Open Sans',Arial,Helvetica,sans-serif;font-size:11px!important;font-weight:700;letter-spacing:0.1em;line-height:20px;margin:0!important;padding:10px!important;width:100%;height:auto;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-horizontalRow button:hover{background-color:#e0e0e0!important;border-color:#e0e0e0!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit{margin:0 0 20px 0;float:left;width:100%;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit button{background-color:#ffffff!important;border:none!important;border-radius:4px!important;box-shadow:none!important;color:#000000!important;cursor:pointer;font-family:'Open Sans',Arial,Helvetica,sans-serif!important;font-size:11px!important;font-weight:700!important;letter-spacing:0.1em;line-height:21px!important;height:auto;padding:10px!important;width:100%!important;box-sizing:border-box!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit button.loading{display:none;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-embedSubmit button:hover{background-color:#e0e0e0!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent h4{color:#ffffff!important;}
#mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-successBody .ml-form-successContent p{color:rgba(255,255,255,0.7)!important;}
.ml-mobileButton-horizontal{display:none;}
#mlb2-40421023 .ml-mobileButton-horizontal button{background-color:#ffffff!important;border-color:#ffffff!important;border-style:solid!important;border-width:1px!important;border-radius:4px!important;box-shadow:none!important;color:#000000!important;cursor:pointer;font-family:'Open Sans',Arial,Helvetica,sans-serif!important;font-size:11px!important;font-weight:700!important;letter-spacing:0.1em;line-height:20px!important;padding:10px!important;width:100%!important;}
.ml-error input,.ml-error textarea,.ml-error select{border-color:red!important;}
@media only screen and (max-width:400px){
  .ml-form-embedWrapper.embedDefault,.ml-form-embedWrapper.embedPopup{width:100%!important;}
  .ml-form-formContent.horozintalForm{float:left!important;}
  .ml-form-formContent.horozintalForm .ml-form-horizontalRow{height:auto!important;width:100%!important;float:left!important;}
  .ml-form-formContent.horozintalForm .ml-form-horizontalRow .ml-input-horizontal{width:100%!important;}
  .ml-form-formContent.horozintalForm .ml-form-horizontalRow .ml-input-horizontal>div{padding-right:0!important;padding-bottom:10px;}
  .ml-form-formContent.horozintalForm .ml-button-horizontal{display:none!important;}
  .ml-mobileButton-horizontal{display:inline-block!important;margin-bottom:20px;width:100%;}
  .ml-form-formContent.horozintalForm .ml-form-horizontalRow .horizontal-fields{margin-bottom:10px!important;width:100%!important;}
  #mlb2-40421023.ml-form-embedContainer .ml-form-embedWrapper .ml-form-embedBody .ml-form-formContent.horozintalForm{padding:0 0 10px 0!important;}
}
</style>'''

html = html.replace(old_css_block, new_css_block)

# ── 2. Update nl-title and nl-sub text ───────────────────────────────────
html = html.replace(
    '<h2 class="nl-title"><span data-i18n="nl.title1">毎ドロップ、</span><em data-i18n="nl.title2">最速通知。</em></h2>',
    '<h2 class="nl-title"><span data-i18n="nl.title1">知る人だけが、</span><em data-i18n="nl.title2">買える。</em></h2>'
)
html = html.replace(
    '<p class="nl-sub" data-i18n="nl.sub">スパムなし。お知らせだけ。</p>',
    '<p class="nl-sub" data-i18n="nl.sub">毎週金曜、DROP前に届く。</p>'
)

# ── 3. Replace ML embed div with horizontal form ─────────────────────────
old_embed = '''  <div id="mlb2-40421023" class="ml-form-embedContainer ml-subscribe-form ml-subscribe-form-40421023">
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
  </div>'''

new_embed = '''  <div id="mlb2-40421023" class="ml-form-embedContainer ml-subscribe-form ml-subscribe-form-40421023">
    <div class="ml-form-align-center">
      <div class="ml-form-embedWrapper embedForm">
        <div class="ml-form-embedBody ml-form-embedBodyHorizontal row-form">
          <div class="ml-form-embedContent" style="margin-bottom:0;"></div>
          <form class="ml-block-form" action="https://assets.mailerlite.com/jsonp/2293748/forms/185764460472828993/subscribe" data-code="" method="post" target="_blank">
            <div class="ml-form-formContent horozintalForm">
              <div class="ml-form-horizontalRow">
                <div class="ml-input-horizontal">
                  <div style="width:100%;" class="horizontal-fields">
                    <div class="ml-field-group ml-field-email ml-validate-email ml-validate-required">
                      <input type="email" class="form-control" data-inputmask="" name="fields[email]" placeholder="Email" autocomplete="email">
                    </div>
                  </div>
                </div>
                <div class="ml-button-horizontal primary">
                  <button type="submit" class="primary" data-i18n="nl.btn">リストに入る</button>
                  <button disabled="disabled" style="display:none;" type="button" class="loading">
                    <div class="ml-form-embedSubmitLoad"></div>
                    <span class="sr-only">Loading...</span>
                  </button>
                </div>
              </div>
            </div>
            <input type="hidden" name="ml-submit" value="1">
            <div class="ml-mobileButton-horizontal">
              <button type="submit" class="primary" data-i18n="nl.btn">リストに入る</button>
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
  </div>'''

html = html.replace(old_embed, new_embed)

# ── 4. Update LANG dict ───────────────────────────────────────────────────
html = html.replace(
    "    'nl.title1': '毎ドロップ、', 'nl.title2': '最速通知。',\n    'nl.sub': 'スパムなし。お知らせだけ。', 'nl.btn': '登録',",
    "    'nl.title1': '知る人だけが、', 'nl.title2': '買える。',\n    'nl.sub': '毎週金曜、DROP前に届く。', 'nl.btn': 'リストに入る',"
)
html = html.replace(
    "    'nl.title1': 'First to know ', 'nl.title2': 'every drop.',\n    'nl.sub': 'No spam. Just drops.', 'nl.btn': 'Subscribe',",
    "    'nl.title1': 'Only those who know, ', 'nl.title2': 'can buy.',\n    'nl.sub': 'Delivered before every Friday DROP.', 'nl.btn': 'Join the list',"
)

with open("templates/prolific/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✓ Patched successfully")
