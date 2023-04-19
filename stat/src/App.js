import './App.css';
import {db} from "./config";
import {useState, useEffect} from 'react';
import { ref,onValue } from 'firebase/database';

function App() {
  const [testdata, settestdata] = useState("");
  useEffect(()=>{
    onValue(ref(db,'/data/battery_data'),(snapshot)=>{
      const data = snapshot.val();
      if(data!=null){
      settestdata(data)}
    })
  },[]);
  console.log(testdata);
  return (
    <div>
      <h1>Hello World!!!!</h1>
      <div>{JSON.stringify(testdata)}</div>
      <div>{testdata.battery_percentage}</div>
    </div>
  );
}

export default App;
