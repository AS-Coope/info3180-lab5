<template>
    <form @submit.prevent="saveMovie" id="movieForm">
        <div class="form-group mb-3">
            <label for="title" class="form-label">
                Movie Title
            </label>
            <input type="text" name="title" id="title" class="form-control">
            <label for="description" class="form-label">
                Movie Description
            </label>
            <textarea name="description" id="description" class="form-control"></textarea>
            <input type="file" class="form-control" name="poster"/>
            <button type="submit" name="submit" class="btn btn-primary">Upload file</button>
        </div>
    </form>
</template>

<script setup>
//const props = defineProps(['movie'])
//const emit = defineEmits(['edit', 'remove'])
    import {ref, onMounted} from "vue";
    let csrf_token = ref("");
    
    onMounted(()=>{
        getCsrfToken();
    })
    function saveMovie() {

        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
        console.log(form_data.poster)
        fetch("/api/v1/movies", { 
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        }) 
        .then(function(response){ 
            return response.json(); 
        }) 
        .then(function(data){ 
            // display a success message 
            console.log(data); 
            //console.log("this runs");
        }) 
        .catch(function(error) { 
            console.log(error); 
        })
    }
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
        .catch(error => { 
            console.log(error); 
        })
    }
</script>