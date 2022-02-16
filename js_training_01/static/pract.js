


function onFormSubmit(){
    
    let formdata = readForm(insertData,resetForm);
    // console.log(formdata);
    
}


function readForm(callback_insertdata, callback_resetdata){
    let formdata = {}
    formdata["car_no"] = document.getElementById("car_no").value;
    formdata["datepicker"] = document.getElementById("datepicker").value;
    formdata["name"] = document.getElementById("name").value;
    formdata["contact"] = document.getElementById("contact").value;
    callback_insertdata(formdata);
    callback_resetdata();
}


function insertData(data){
    let table = document.getElementById("tb_id").getElementsByTagName("tbody")[0];
    let newrow = table.insertRow(table.length);
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            cell1 = newrow.insertCell(0);
            cell1.innerHTML = data.car_no;
            cell2 = newrow.insertCell(1);
            cell2.innerHTML = data.datepicker;
            cell3 = newrow.insertCell(2);
            cell3.innerHTML = data.name;
            cell4 = newrow.insertCell(3);
            cell4.innerHTML = data.contact;
            let error=false;
            if(!error){
                alert("Loading...");
                resolve();
                
            }
            else{
                reject("Data isn't inserted");
            }
        },5000);
    });
    
    
    
}
function resetForm(){
    document.getElementById("car_no").value = "";
    document.getElementById("datepicker").value = "";
    document.getElementById("name").value = "";
    document.getElementById("contact").value = "";
}

