import './App.css';
import {db} from "./config";
import {useState, useEffect} from 'react';
import { ref,onValue } from 'firebase/database';
import {PieChart, Pie, Legend, Tooltip, BarChart,CartesianGrid,XAxis,YAxis,Bar,Line,LineChart} from 'recharts';
import axios from 'axios';
import sampledata from './ramdata.json';
import sampledata1 from './joee.json';



function App() {
  const [testdata, settestdata] = useState({});
  const [test1,settest1] = useState([]);

  
  useEffect(()=>{
    onValue(ref(db,'/data'),(snapshot)=>{
      const data = snapshot.val();
      if(data!=null){
      settestdata(data)}
    })
    onValue(ref(db,'/sysdata/ram'),(snapshot)=>{
      const data = snapshot.val();
      if(data!=null){
      settest1(data)}
    })
  },[]);
  console.log(test1);
  
                              
  
  return (
    <div>
      <h1>Hello World!!!! welcome to istat</h1>
      <div>{JSON.stringify(testdata)}</div>
      {/* <div>{testdata.free}</div> */}
      {Object.keys(test1).map((id)=>{
        return (
          <>
            <div>{test1[id].active_memory}</div>
          </>
        )            
      })}
      {/* <div>{JSON.stringify(test1)}</div> */}
      
      {/* {testdata !== null?<div>{testdata.battery_data.battery_percent}</div>:<div>nope</div>} */}
      {/* <div>{testdata.battery_data.time_left}</div> */}
      
    

      <BarChart width={730} height={250} data={test1}>
    <CartesianGrid strokeDasharray="3 3" />
    <XAxis/>
    <YAxis />
    <Tooltip />
    <Legend />
    <Bar dataKey="active_memory" fill="#8884d8" />
    <Bar dataKey="available_memory" fill="#82ca9d" />
  </BarChart>

  <LineChart width={730} height={250} data={test1}
  margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
  <CartesianGrid strokeDasharray="3 3" />
  <XAxis />
  <YAxis />
  <Tooltip />
  <Legend />
  <Line type="monotone" dataKey="active_memory" stroke="#8884d8" />
  <Line type="monotone" dataKey="available_memory" stroke="#82ca9d" />
</LineChart>
        
    </div>
  );
}

export default App;
