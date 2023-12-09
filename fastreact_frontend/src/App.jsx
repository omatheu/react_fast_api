import axios from "axios";
import { useState, useEffect } from "react";

function App() {
  const [body, setBody] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:7777/get_data")
      .then((response) => {
        const data = response.data
        setBody(data['body'])
      })
      .catch((e) => {
        //Placeholder
      });
  }, []);

  return (
    <div>
      <p>Texto</p>
      {body}
    </div>
  );
}

export default App;
