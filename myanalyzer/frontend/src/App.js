import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import TextFieldComponent from './components/TextFieldComponent';
import SubmitButton from './components/SubmitButton';
import ResetButton from './components/ResetButton';
import axios from 'axios';
const styles={
  resetbtn:{
    'margin':'20px'
  }
}
class App extends Component {
  constructor(props) {
      super(props);
      this.state = {
          data:'',
          result:''
      };
      axios.defaults.xsrfCookieName = 'csrftoken';
      axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    }

    handlechange(event){
      this.setState({data:event.target.value,result:''})
    }
    onSubmitClick(){
      if(this.state.data !== ""){
        axios.post('/analyzedata',{
          data:this.state.data
        }).then((res)=>{
          console.log(res);
          this.setState({result:res.data})
        });
      }
    }
    onResetClick(){
      this.setState({result:'',data:''})
    }


  render() {
    let resultClass = this.state.result==="Positive" ? "success":"failure";

    let result = this.state.result === "" ? '':<span>Result: <span className={resultClass}>{this.state.result}</span></span>;
    return (
      <div className="App">
        <header className="App-header">
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500"></link>
          <h1 className="App-title">Welcome to Comment Analyzer</h1>
        </header>
       
            <TextFieldComponent 
              data={this.state.data} 
              handleChange ={this.handlechange.bind(this)}
            />
            <div>
             <ResetButton onClick = {this.onResetClick.bind(this)} style={styles.resetbtn}/>
            
            <SubmitButton onClick = {this.onSubmitClick.bind(this)}/>
            <br /><br />
            </div>
            {result}
        
      </div>
    );
  }
}

export default App;