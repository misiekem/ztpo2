var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) { 
    
    //check connection
    $scope.init = function(){
        $http({
            method: "GET",
            dataType: 'JSONP', 
            url: "http://localhost:5000/"
        }).then(function(data){
            $scope.connected = "ALL DAY LONG KURWA";
        }, function(error){
            $scope.connected = "Missing connection. Please refresh or restart flask server.";
        });
    }
    
    //get data
    $scope.getData = function(){
        $scope.show = false;
        $scope.show1 = false;
        $scope.show2 = false;
        $scope.show3 = false;
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
                alert("Something gones wrong");
            })
        }else{
            $scope.show = true;
        }
        
    }
});