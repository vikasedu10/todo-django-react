import http from '../HttpCommon';

class TutorialDataService {
    getNotes () {
        return http.get("notes/");
    }

    getNote (id) {
        return http.get(`notes/${id}`);
    }

    createNote (data) {
        return http.post("notes/", data);
    }

    updateNote (id, data) {
        return http.put(`notes/${id}`, data);
    }

    deleteNote (id) {
        return http.delete(`notes/${id}`)
    }

    deleteNotes () {
        return http.delete('notes/')
    }

    findNote(searchText) {
        return http.get(`/tutorials?data=${searchText}`);
      }
}

export default new TutorialDataService();