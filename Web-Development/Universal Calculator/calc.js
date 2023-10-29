function cosFunction() {
    var targetId = document.getElementById('input-box').value;
    var check = /^[+-]?\d+(\.\d+)?$/.test(targetId);
    if(check === true) {
    
    document.getElementById('input-box').value = Math.cos(targetId);
    
    }
    else {
    alert('Please enter a valid number');
    
    }
    }
    function sinFunction() {
    var targetId = document.getElementById('input-box').value;
    var check = /^[+-]?\d+(\.\d+)?$/.test(targetId);
    if(check === true) {
    
    document.getElementById('input-box').value = Math.sin(targetId);
    
    }
    else {
    alert('Please enter a valid number');
    
    }
    }
    function tanFunction() {
    var targetId = document.getElementById('input-box').value;
    var check = /^[+-]?\d+(\.\d+)?$/.test(targetId);
    if(check === true) {
    
    document.getElementById('input-box').value = Math.tan(targetId);
    
    }
    else {
    alert('Please enter a valid number');
    
    }
    }
    function lnFunction() {
    var targetId = document.getElementById('input-box').value;
    var check = /^[+-]?\d+(\.\d+)?$/.test(targetId);
    if(check === true) {
    
    document.getElementById('input-box').value = Math.log(targetId);
    
    }
    else {
    alert('Please enter a valid number');
    
    }
    }
    function logFunction() {
    var targetId = document.getElementById('input-box').value;
    var check = /^[+-]?\d+(\.\d+)?$/.test(targetId);
    if(check === true) {
    
    document.getElementById('input-box').value = Math.log10(targetId);
    
    }
    else {
    alert('Please enter a valid number');
    
    }
    }
    function sqrtFunction() {
    var targetId = document.getElementById('input-box').value;
    var check = /^[+-]?\d+(\.\d+)?$/.test(targetId);
    if(check === true) {
    
    document.getElementById('input-box').value = Math.sqrt(targetId);
    
    }
    else {
    alert('Please enter a valid number');
    
    }
    }
    function factorialFunction() {
    var targetId = document.getElementById('input-box').value; 
    var check = /^\d+$/.test(targetId);
    if (check === true) { 
    var factorial = 1;
    for(i = 1;i <= targetId;i++) {
    factorial = factorial * i;
    }
    document.getElementById('input-box').value = factorial;
    }
    else {
    alert('Please enter a valid number or non-floating point number');
    
    }
    
    }