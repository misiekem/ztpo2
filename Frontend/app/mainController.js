var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) { 
    
    //check connection
    $scope.init = function(){
        $http({
            method: "GET",
            dataType: 'JSONP', 
            url: "http://localhost:5000/"
        }).then(function(data){
            $scope.connected = "Połączono";
        }, function(error){
            $scope.connected = "Brak połączenia. Uruchom lub zrestartuj serwer Flask";
        });
    }
    
    //get data
    $scope.getData = function(){
        $scope.show = false; // show alert about missing variables
        $scope.show1 = false; // show alert about missing user in biblos db
        $scope.show2 = false; // show alert about possible delay with delivery user info
        $scope.show3 = false; // show detailed information about founded user
        if($scope.surname||$scope.name){
            $scope.show2 = true;
            $http({
                method: "GET",
                dataType: 'JSONP',
                url: "http://localhost:5000/user?surname=" + $scope.surname+"&name="+$scope.name
            }).then(function(data){
                if(data.data['id']==='None'){
                    $scope.show1 = true;
                    $scope.show2 = false;
                }else{
                    $scope.show3 = true;
                    $scope.dane = data.data;
                    $scope.pubs = $scope.dane['publications'];
                    $scope.show2 = false;
                }                
            }, function(error){
                console.log(error);
                alert("Something gones wrong. Please refresh page");
            })
        }else{
            $scope.show = true;
        }
        
    }
});