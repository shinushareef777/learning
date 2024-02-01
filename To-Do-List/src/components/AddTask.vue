<template>
    <form autocomplete="off"  @submit="onSubmit" class="add-form">
      <div class="form-control">
            <label for="">Categories</label>
            <!-- <input v-model="text" type="text" name="text" placeholder="Add Task"> -->
            <select name="" id="" v-model="categories" placeholder="Select Category">
              <option value="Grocery">Grocery</option>
              <option value="Study">Study</option>
              <option value="Creative">Creative</option>
            </select>
        </div>
        <div class="form-control">
            <label for="">Task</label>
            <input v-model="text" type="text" name="text" placeholder="Add Task">
        </div>
        <div class="form-control">
            <label for="">Day & Time</label>
            <input v-model="day" type="text" name="day" placeholder="Add Day & Time">
        </div>
        <div class="form-control form-control-check">
            <label for="">Reminder</label>
            <input type="checkbox" name="reminder" v-model="reminder" >
        </div>
        <input type="submit" class="btn btn-block">
    </form>
</template>

<script>
    export default{
        name: 'AddTask',
        data(){
            return{
                text: '',
                day: '',
                reminder: false,
                categories: '',
                completed:false,
            }
        },
        methods: {
            onSubmit(e){
                e.preventDefault()
                if (!this.text){
                    alert("Please enter a task")
                    return
                }
                const newTask = {
                    text: this.text,
                    day: this.day,
                    reminder: this.reminder,
                    categories: this.categories,
                    completed: this.completed
                }
                this.$emit('add-task', newTask)
                this.text = ''
                this.day = ''
                this.reminder = false
                this.categories = ''
            }
        }
    }
</script>


<style scoped>
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 20px 0;
}
.form-control label {
  display: block;
}
.form-control input, select {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}

.form-control input:focus{
  outline: steelblue;
}

.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.form-control-check label {
  flex: 1;
}
.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
