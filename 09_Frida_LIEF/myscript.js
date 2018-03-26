'use strict';

console.log("Waiting for Java..");

while(!Java.available) {
  console.log("Not available...");
}

Java.perform(function () {

  var Log = Java.use("android.util.Log");
  Log.v("frida-lief", "I'm in the process!");

});



