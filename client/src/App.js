import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import DataManipulationPage from './DataManipulate';
import { ChromaDBData, ChromaDBDataDisplay } from './getChromadbData'

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<DataManipulationPage />} />
        <Route exact path="/chroma" element={<ChromaDBData />} />
        <Route exact path="/chromaAll" element={<ChromaDBDataDisplay />} />
        {/* other routes... */}
      </Routes>
    </Router>
  );
}

export default App;