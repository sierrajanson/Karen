import {React, useState, useEffect} from 'react';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition';
import '../App.css';


const Karen = () =>{
  const {
      transcript,
      listening,
      resetTranscript,
      browserSupportsSpeechRecognition
  } = useSpeechRecognition();

    useEffect(()=>{     // on change, log what is being said to verify that microphone is working
      console.log(transcript);
    })
    return ( // can give startListening method argument of "{continuous: true}" so it doesn't listening after it detects that you've stopped speaking
    <div >
      <div className="microphone_buttons"> 
        <button onClick={SpeechRecognition.startListening}>Start</button>
        <button onClick={SpeechRecognition.stopListening}>Stop</button>
      </div>
      <h1> :) </h1>
    </div>
  );
}
export default Karen;
