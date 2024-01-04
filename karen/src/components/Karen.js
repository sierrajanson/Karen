import {React, useState, useEffect} from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import '../App.css';
import api from '../api';

const Karen = () => {
    const {
        transcript,
        listening,
        resetTranscript,
        browserSupportsSpeechRecognition
    } = useSpeechRecognition();
    const [sentiment,moodSwing] = useState(".__.");

    const fetchDat = async (input_text) => {
      const resp = await api.get('/testing/',{
        params: {input_data:input_text},
      });
      console.log(resp.data.emotion);
      if (resp.data.emotion === "POSITIVE!"){
        moodSwing("^__^");
      }
      else{
        moodSwing("u__u");
      }
    }

    // useEffect(()=>{
    //   fetchDat();
    // },[]);
    
    const handleDone = () => {
      console.log(transcript);
      SpeechRecognition.stopListening();
      fetchDat(transcript);
    }      

    return ( // can give startListening method argument of "{continuous: true}" so it doesn't listening after it detects that you've stopped speaking
    <div>
      <div className="microphone_buttons"> 
        <button onClick={SpeechRecognition.startListening}>Start</button>
        <button onClick={(e) => handleDone()}>Stop</button>
      </div>
      <div className="face">{sentiment}</div>
    </div>
  );
}
export default Karen;
