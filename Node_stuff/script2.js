var app = angular.module('Friends',[]);
app.controller('friendsController', function($scope, $http) {
    $http.get('/getData').then(function(data) {
        $scope.friends = data;
    });
});
