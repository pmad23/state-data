var app = angular.module('Friends',[]);
app.controller('friendsController', function($scope, $http) {
  $scope.data = {};
   $scope.submit = function(){
      console.log('clicked submit');
      $http({
          url: 'http://localhost:5000/friendships',
          method: 'POST'
          data: $scope.data
      }).then(function(httpResponse) {
          console.log('response:', httpResponse);
      })
  }
});


