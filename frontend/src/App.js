import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/navbar/Navbar';
import Homepage from './pages/Homepage';
import Feature from './pages/Feature';


function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path='/' component={Homepage} />
        <Route path='/feature' exact component={Feature} />
      </Routes>
    </Router>
  );
}

export default App;
