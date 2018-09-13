import React from 'react';
import TextField from '@material-ui/core/TextField';

const styles = {
  textfield:{
    'minWidth': '450px',
    'margin': 'auto',
    'maxWidth': '200px'
  }
}

const TextFieldComponent =({handleChange,data})=>{
    // constructor(props) {
    //   super(props);
    //   this.state = {
    //       data:''
    //   };
    // }

    // (event){
    //     this.setState({data:event.target.value})

    // }

        return (
          <div style={styles.textfield}>
            <TextField
                id="name"
               
                InputProps={
                  {
                    style:{
                      minWidth: '100px'}
                  }
                }
                fullWidth={true}
                label="Enter Your Comment"
                multiline={true}
                onChange={handleChange}
                margin="normal"
                value={data}
                />
          </div>
        );
      }
   
  
export default TextFieldComponent;
  