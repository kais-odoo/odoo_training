
let formdata;
let table = document.getElementById("tb_id").getElementsByTagName("tbody")[0];
var xhttp = new XMLHttpRequest();

document.getElementById("reset").addEventListener("click",()=>{
    resetForm();
});
function onFormSubmit(){
    
    formdata = readForm(insertData,resetForm);
    console.log(formdata);
    


    
    
    
      
    
}


async function readForm(callback_insertdata, callback_resetdata){
    let formdata = {}
    formdata["car_no"] = document.getElementById("car_no").value;
    formdata["datepicker"] = document.getElementById("datepicker").value;
    formdata["name"] = document.getElementById("name").value;
    formdata["contact"] = document.getElementById("contact").value;
    formdata["cars_type"] = document.getElementById("cars_type").value;
    callback_insertdata(formdata);
    const res = await loadDoc(formdata);
    callback_resetdata();
    
    

}


function insertData(data){
   
    let newrow = table.insertRow(table.length);
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            
            if(data.car_no != "" && data.datepicker != "" && data.name != "" && data.contact != "" && data.cars_type != ""){
                resolve();
                
            }
            else{
                
                reject("Data isn't inserted");
            }
        },3000);
    }).then(()=>{
                cell1 = newrow.insertCell(0);
                cell1.innerHTML = data.car_no;
                cell2 = newrow.insertCell(1);
                cell2.innerHTML = data.datepicker;
                cell3 = newrow.insertCell(2);
                cell3.innerHTML = data.name;
                cell4 = newrow.insertCell(3);
                cell4.innerHTML = data.contact;
                cell5 = newrow.insertCell(4);
                cell5.innerHTML = data.cars_type;
                
    },()=>{
        alert("Data is missing")
    });
    
    
    
}
function resetForm(){
    document.getElementById("car_no").value = "";
    document.getElementById("datepicker").value = "";
    document.getElementById("name").value = "";
    document.getElementById("contact").value = "";
    document.getElementById("cars_type").value = "";
}
function loadDoc(data) {
    return new Promise((resolve)=>{
        xhttp.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200) {
                getOffer(this, data.cars_type);
                resolve();
              }
            };
            xhttp.open("GET", "/static/pract.xml", true);
            xhttp.send();
    })
    
  }
  function getOffer(xml,carType) {
    var xmlDoc = xml.responseXML;
    var suv_offer =xmlDoc.getElementsByTagName("suv")[0].childNodes[0].nodeValue;
    var muv_offer =xmlDoc.getElementsByTagName("muv")[0].childNodes[0].nodeValue;
    var sedan_offer =xmlDoc.getElementsByTagName("sedan")[0].childNodes[0].nodeValue;
    if(carType == "suv"){
            document.getElementById("marquee_text").innerHTML = suv_offer;
    }
    else if(carType == "muv"){
        document.getElementById("marquee_text").innerHTML = muv_offer;
    }
    else if(carType == "sedan"){
        document.getElementById("marquee_text").innerHTML = sedan_offer;
    }
    else{
        console.log("something went wrong");
    }
        
  }
