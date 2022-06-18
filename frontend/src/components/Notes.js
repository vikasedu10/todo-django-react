import React from 'react'
import axios from 'axios';

const baseURL = "http://localhost:8000/api/notes/"

export const Notes = () => {
    const [notes, setNotes] = React.useState([])

  return (
    <>
    <div className='container col-sm-8 col-md-4 my-3'>

        <div>Notes</div>
        <p>Note 1</p>
        <p>Note 2</p>
        <p>Note 3</p>
        <p>etc...</p>
    </div>
    </>
  )
}
