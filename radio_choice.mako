# -*- coding: utf-8 -*-
<ul class="deformSet">
    <input type="hidden" name="__start__" value="${field.name}:rename"/>
    % for index, choice in enumerate(field.widget.values):
        <li class="deformSet-item">
          <input
            % if choice.value == cstruct:
            checked="checked"
            % endif
            % if field.widget.css_class:
            class="${field.widget.css_class}"
            % endif
            type="radio"
            name="${field.oid}"
            value="${choice.value}"
            id="${field.oid}-${index}"/>
          <label for="${field.oid}-${index}">${choice.title}</label>
        </li>
    % endfor
    <input type="hidden" name="__end__"/>
</ul>

