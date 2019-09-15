var NotesButton = document.getElementById('NotesButton');
var SharedButton = document.getElementById('SharedButton');
var SettingsButton = document.getElementById('SettingsButton');
var AccountButton = document.getElementById('AccountButton');

NotesButton.style.opacity = '1';

NotesButton.addEventListener('click', function () {
    NotesButton.style.opacity = '1';
    SharedButton.style.opacity = '0.5';
    SettingsButton.style.opacity = '0.5';
    AccountButton.style.opacity = '0.5';
})

SharedButton.addEventListener('click', function () {
    NotesButton.style.opacity = '0.5';
    SharedButton.style.opacity = '1';
    SettingsButton.style.opacity = '0.5';
    AccountButton.style.opacity = '0.5';
})

SettingsButton.addEventListener('click', function () {
    NotesButton.style.opacity = '0.5';
    SharedButton.style.opacity = '0.5';
    SettingsButton.style.opacity = '1';
    AccountButton.style.opacity = '0.5';
})

AccountButton.addEventListener('click', function () {
    NotesButton.style.opacity = '0.5';
    SharedButton.style.opacity = '0.5';
    SettingsButton.style.opacity = '0.5';
    AccountButton.style.opacity = '1';
})