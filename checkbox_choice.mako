# -*- coding: utf-8 -*-
<input type="hidden" name="__start__" value="${field.name}:sequence"/>
  <ul class="deformSet">
    % for index, choice in enumerate(field.widget.values):
    <li class="deformSet-item">
      <input
        % if choice.value in cstruct:
        checked="checked"
        % endif
        % if field.widget.css_class:
        class="${field.widget.css_class}"
        % endif
        type="checkbox"
        name="checkbox"
        value="${choice.value}"
        id="${field.oid}-${index}"/>
      <label for="${field.oid}-${index}">${choice.title}</label>
    </li>
    % endfor
  </ul>
<input type="hidden" name="__end__" value="${field.name}:sequence"/>

