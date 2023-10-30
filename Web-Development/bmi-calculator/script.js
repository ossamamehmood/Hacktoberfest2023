$(function(){

	$('button').bind('click', function(){

		var altura = $('#altura').val();
		var peso = $('#peso').val();

		//Recoloca '.'(ponto) quando for digitado ','()vírgula
		altura = altura.replace(',','.');
		peso = peso.replace(',','.');

		//IMC = peso / altura²
		var imc = peso / (altura*altura);

		
		if(imc < 16){
			var traducao = 'Low weight, very serious';
		} else if(imc >= 16 && imc < 17){
			var traducao = 'Low weight, serious';
		} else if(imc >= 17 && imc < 18.50){
			var traducao = 'Low weight';
		} else if(imc >= 18.50 && imc < 25){
			var traducao = 'Normal weight';
		} else if(imc >= 25 && imc < 30){
			var traducao = 'Overweight';
		} else if(imc >= 30 && imc < 35){
			var traducao = 'Grade I obesity';
		} else if(imc >= 35 && imc < 40){
			var traducao = 'Grade II obesity';
		} else if(imc >= 40){
			var traducao = 'Grade III obesity';
		}
		

		$('#resultado').html("Your BMI is: "+imc.toFixed(2)+" kg/m² and your status is: "+traducao);


	});

});