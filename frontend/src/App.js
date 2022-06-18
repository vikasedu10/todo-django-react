import { Header } from './components/Header';
import { Notes } from './components/Notes';
import { Note } from './components/Note';
import { AddNote } from './components/AddNote';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
function App() {
  return (
    <>
    <Router>
      <Header title="| Todos |" />
      <Routes>
        <Route path='/' element={<Navigate to="/notes" />} />
        <Route path='/notes' element={<Notes />} />
        <Route path='/notes/:id' element={<Note />} />

        <Route path='/addNote' element={<AddNote />} />
      </Routes>
    </Router>
    </>
  );
}

export default App;
