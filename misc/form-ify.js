function automateInput(){
    var mainForm = document.createElement('form');
    var header_input = document.createElement('input');
    var content_input = document.createElement('input');
    header_input.type = 'text';
    content_input.type = 'text';
    header_input.value = /*String for header value*/"";
    content_input.value = /*String for content value*/"";
    header_input.name = 'header';
    content_input.name = 'content';
    var submit_btn = document.createElement('input');
    submit_btn.type = 'submit';
    submit_btn.value = 'Submit';
    mainForm.appendChild(header_input);
    mainForm.appendChild(content_input);
    mainForm.appendChild(submit_btn);
    var body = document.body;
    body.appendChild(mainForm);
    submit_btn.click()
    body.removeChild(mainForm);
}
