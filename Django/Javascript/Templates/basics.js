//alert("Welcome To Canada Account")
//var deposit = prompt("Enter The Amount You Want To Deposited:")
//alert("Deposited Amount is"+deposit)
//console.log("You Are Lucky Guy")
//var Withdrawn = prompt("Enter The Amount You Want To Withdrawn:")
//var total=deposit-Withdrawn
//console.log("Total Amount is"+total)

//var lbs = prompt("Enter the Weight in lbs:")
//var kg=lbs*0.454
//alert("This is :"+kg+"Kilograms")
//console.log("Conversion Completed!")

//var hot = false;
//var temp = 55;

//if (temp > 55) {
//    console.log("Its Very Hot Outside!");
//}else if (temp>=55 && temp<=55) {
//    console.log("Average Hot!");
//}else if (temp<=55 || temp>=35) {
//    console.log("Its normal Outside!")
//}
//else {
//    console.log("Its Very Cool Outside!");
//}

//if (true) {
//    hot = false
//}
//console.log(hot)

//var cheese = 20;
//var curd = 20;
//var report = "Blank";
//
//if(cheese == 20 && curd != 20){
//    report="Sales is equal!"
//}else if(cheese <= 30 || curd >= 30){
//    report="Sales is not equal!"                     //If,else if & else  statements in javascript
//}else{
//    report = "Sales is very high!"
//}
//console.log(report);

//var x = 0
//while (x < 10) {
//    console.log("Currently X Is In:"+x);
//    if (x == 5) {
//        console.log("X Is Equal To 5!");
//        break;
//    }
//    console.log("Still X Is Less Than 5 Add 1 To X !")    //While statement in javascript
//    x = x + 1
//}

//var num = 0;
//while (num < 10) {
//    if (num % 2 == 0){
//        console.log(num)                  //Nested if statement
//    }
//    console.log("Even numbers are:"+num)
//    num += 1
//}

//for(var num = 0;num<=10;num++){
//    console.log("Number is:"+num)
//}

//var word = "ABABABABABABA"
//for(i=0; i<word.length; i+=2){
//    console.log(word[i])
//}

//var x=0;
//while (x<5){
//    console.log("Hello:")
//    x++
//}
//for(var i = 0;i < 5;i++){
//    console.log("Hello")
//}

//var x=1
//while (x<25){
//    if (x%2 != 0){
//        console.log(x)
//    }
//    x += 1
//}

//for (var i = 1;i < 25;i++){
//    if(i%2 != 0){
//        console.log(i)
//    }
//}

//JavaScript project
//first_name = prompt("Please Enter The First Name:")
//last_name = prompt("Please Enter The Last Name:")
//age = prompt("Please Enter Your Age:")
//height = prompt("Please Enter Your Height:")
//pet_name = prompt("Please Enter Your Petname:")
//alert("Thank You For Giving Imformation!")

//name_cond = null;               //Check all four conditions
//age_cond = null;
//height_cond = null;
//pet_cond = null;

//if(first_name[0] === last_name[0]) {
//    name_cond = true;
//}else{
//    name_cond = false;
//}

//if(age > 30 && age < 20) {
//    age_cond = true;
//}else {
//    age_cond = false;
//}

//if(height > 175) {
//    height_cond =true;
//}else {
//    height_cond = false;
//}

//if (pet_name[pet_name.length-1] === 'y') {
//    pet_cond = true;
//}else {
//    pet_cond = false;
//}

// Check All Conditions
//if(name_cond && age_cond && height_cond && pet_cond) {
//    console.log("Welcome Spy!")
//}else {
//    console.log("Nothing To See Here!")
//}

//function fun(name) {             //Functions in javascript
//    console.log("Hello"+name)
//    return "Hello"+name
//}

//function addnum(num1,num2) {
//    console.log(num1 + num2)
//    return num1+num2
//}

//function fun(name="Saikumar",title="sir") {
//    console.log(title+ "" +name)
//    return(title+ ""+name)
//}

//function fun(num) {
//    var result = num*5
//    console.log(result)
//}

//var s ="Global s"
//var k ="Global k"

//function fun(k) {
//    console.log(s)
//    k="Global Inside Function"
//    console.log(k)
//}
//fun()
//console.log(k)

//Exercise Solutions
//function sleep(a,  b) {
//    return (a! || b)
//}
//function monkey(as, bs) {
//    return (as && bs) || (!as && !bs)
//}

//function fun(str,n) {
//    return(sai,3)
//    var count="";
//    var i = 1;
//    while(i<n) {
//        count +=str
//        i++
//    }
//    return count
//}
//fun(sai,3)

//function fun(a,b,c) {
//    if(a==13) {
//        return 0
//    }else if(b==13) {
//        return a
//    }else if(c==13) {
//        return a+b
//    }else {
//        return a+b+c
//    }
//}

//function fun(speed,birth) {
//    if(birth) {
//        speed -= 5
//    }
//    if(speed<=60) {
//        return 0
//    }
//    if(60 < speed <= 80) {
//        return 1
//    }
//    return 2
//}

//function fun(s,b,g) {
//    return(g%5>=0 && g%5-s <= 0 && s+5*b>=g)
//}

// Array Roaster Web App Exercise Solution
//var Roaster =[]

//function AddNew() {
//    NewName = prompt("Would You Like To Add The Name?");
//    Roaster.push(NewName);
//}

//function Remove() {
//    RemName = prompt("Would You Like To Remove Name?")
//    var index = Roaster.indexOf(RemName);
//    Roaster.splice(index,1);
//}

//function Display() {
//    console.log(Roaster);
//}

//var start = prompt("Would You Like You Play Roaster WebApp?Press(y/n)");
//var request = "empty";
//if(start == 'y') {
//    while(request != 'quit') {
//        request = prompt("Please Select Your option: Add, Remove,Display & quit:");

//        if(request=='Add') {
//            AddNew();
//        }else if (request == 'Remove') {
//            Remove();
//        }else if(request=='Display') {
//            Display()
//        }else {
//            alert("Not Recognized");
//            //request="quit"
//        }
//    }

//}
//alert("Thank You For Using Web App! PLease Refresh To Start Over!");

//New = {
//    Name:"Saikumar",
//    Age:"22",
//    Job:"Python Full Stack Devolper",
//   Greet:function(){
//        console.log("Hello"+this.Name);
//    }
//    NameLength:function(){
//        console.log(this.Name.length);
//    }
//    Type:function(){
//        console.log("Name is:"+this.Name,"Age is:"+this.Age,"Job is:"+this.Job);
//    }
//}
//Sample = {
//    a : "Hello, Javascript World!",
//    method : function(){
//        console.log("New Method");
//    }
//    Type: function(){
//        console.log(this.a.split(" "));
//    }
//}