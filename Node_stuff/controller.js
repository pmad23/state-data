var app = angular.module('myApp',[]);
app.controller('RadialGaugeCtrl', ['$scope', function ($scope) { 
	$scope.value = 20; 
	$scope.upperLimit = 100; 
	$scope.lowerLimit = 0; 
	$scope.unit = "C/F"; 
	$scope.precision = 2; 
	$scope.ranges = [ { 
		min: 0, 
		max: 10, 
		color: '#DEDEDE' }, 
		{ 
		min: 10, 
		max: 20, 
		color: '#8DCA2F' 
		}, 
		{ 
		min: 20, 
		max: 30, 
		color: '#FDC702' 
		}, 
		{ min: 30, 
		max: 40, 
		color: '#FF7700' 
		}, 
		{ min: 40, 
		max: 50, 
		color: '#C50200' } ]; 
}]);
