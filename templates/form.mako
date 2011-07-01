# -*- coding: utf-8 -*-
<%
rndr = field.renderer
tmpl = field.widget.item_template
%>
<form \
id="${field.formid}" \
action="${field.action}" \
method="${field.method}" \
enctype="multipart/form-data" \
accept-charset="utf-8" \
i18n:domain="deform"\
% if field.css_class:
 class="${field.css_class}"\
% endif
>

  <fieldset class="deformFormFieldset">
    % if field.title:
    <legend>${field.title}</legend>
    % endif

    <input type="hidden" name="_charset_" />
    <input type="hidden" name="__formid__" value="${field.formid}"/>
    <ul>

      % if field.error:
      <li class="errorLi">
        <h3 class="errorMsgLbl" i18n:translate=""
            >There was a problem with your submission</h3>
        <p class="errorMsg" i18n:translate=""
           >Errors have been highlighted below</p>
      </li>
      % endif

      % if field.title:
      <li class="section first">
        <h3>${field.title}</h3>
        % if field.description:
        <div>${field.description}</div>
        % endif
      </li>
      % endif

      % for f in field.children:
      ${rndr(tmpl, field=f, cstruct=cstruct.get(f.name, null))}
      % endfor

      <li class="buttons">
        % for button in field.buttons:
          <button
              % if button.disabled:
                 disabled="disabled"
              % endif
              id="${field.formid+button.name}"
              name="${button.name}"
              type="${button.type}"
              class="btnText submit"
              value="${button.value}">
            <span>${button.title}</span>
          </button>
        % endfor
      </li>

    </ul>

  </fieldset>

% if field.use_ajax:
<script type="text/javascript">
  deform.addCallback(
     '${field.formid}',
     function(oid) {
         var options = {
           target: '#' + oid,
           replaceTarget: true,
         };
         var extra_options = ${field.ajax_options};
         var name;
         if (extra_options) {
           for (name in extra_options) {
             options[name] = extra_options[name];
           };
         };
         $('#' + oid).ajaxForm(options);
   });
</script>
% endif

</form>
