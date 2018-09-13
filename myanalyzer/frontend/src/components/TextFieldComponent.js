import React from 'react';
import TextField from '@material-ui/core/TextField';

const styles = {
  textfield:{
    'width':'30%',
    'margin':'auto'
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
  