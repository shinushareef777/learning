import { createApp } from "vue";
import { createStore } from "vuex";

const store = createStore({
  state: {
    todos: [
      {id: 1, text: 'Learn Vue', done: true},
      {id: 2, text: 'Learn Node Js', done: true},
    ]
  },
  getters: {
    doneTodos(state) {
      return state.todos.filter(todo => todo.done)
    },
    doneTodosCount(state, getters) {
      return getters.doneTodos.length
    }
  }
})

console.log(store.getters.doneTodosCount)