function fillBirthDate() {
    document.addEventListener('DOMContentLoaded', function(event) {
        document.getElementById('id_Birth_date').addEventListener('focus', autofillBirthDate)})
}

function fillPercent() {
    document.addEventListener('DOMContentLoaded', function(event) {
        document.getElementById('id_FK_Id_account_type').addEventListener('change', autofillPercent)})
}

function autofillBirthDate() {
    let pesel = document.getElementById('id_Pesel').value
    if (pesel.length == 11 && containsOnlyDigits(pesel) ) {
        let year = pesel.substr(0,2)
        let month = pesel.substr(2,2)
        let day = pesel.substr(4,2)
        if (parseInt(month) > 12) {
            year = '20' + year
            month = (parseInt(month) - 20).toString().padStart(2,0)}
        else {
            year = '19' + year
        }
        document.getElementById('id_Birth_date').value = year + '-' + month + '-' + day}
}

function autofillPercent() {
    var data = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'))
    var val = data[document.getElementById('id_FK_Id_account_type').value]
    if (val) {
        document.getElementById('id_Percent').value =  val}
    else { 
        document.getElementById('id_Percent').value = 0}
}

function containsOnlyDigits(str) {
    return !isNaN(str) && !isNaN(parseFloat(str));
  }
