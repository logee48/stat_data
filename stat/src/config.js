import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";

const firebaseConfig = {
    apiKey: "AIzaSyCZ5jjDEDdvsqshdXOHq6fae0J0RpyRMhE",
    authDomain: "pythonconn-2578e.firebaseapp.com",
    databaseURL: "https://pythonconn-2578e-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "pythonconn-2578e",
    storageBucket: "pythonconn-2578e.appspot.com",
    messagingSenderId: "730718512019",
    appId: "1:730718512019:web:b4693c6da109e53c0a7e66",
    measurementId: "G-WE7HWKZMRT"
  };
  

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
export {db};