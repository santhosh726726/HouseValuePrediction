  function calculatePrice() {
    console.log("Estimate price button clicked");
    var areaIncome = document.getElementById("areaIncome").value;
    var houseAge = document.getElementById("houseAge").value;
    var noOfRooms = document.getElementById("noOfRooms").value;
    var noOfBedRooms = document.getElementById("houseAge").value;
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict"; 
    $.post(url, {
        areaIncome: areaIncome,
        houseAge: houseAge,
        noOfRooms: noOfRooms,
        noOfBedrooms: noOfBedRooms
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }