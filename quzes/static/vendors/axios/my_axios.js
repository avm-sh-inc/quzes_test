axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true

function placeholder(text = null, animate = null) {
    if (animate === null){
        const preloader = document.createElement('div');
        preloader.id = 'preloader';

        const loader = document.createElement('div');
        loader.id = 'loader';
        preloader.append(loader);

        const text_preloader = document.createElement('div');
        text_preloader.classList.add('col-12');
        text_preloader.classList.add('text-center');
        if (text === null){
            text_preloader.innerHTML = '<h4>Получаем данные с сервера, подождите ...</h4>';
        } else {
            text_preloader.innerHTML = '<h4>'+ text +'</h4>';
        }
        preloader.append(text_preloader);
        return preloader;
    } else {
        animate.childNodes[3].innerText = text;
        return animate;
    }
}

function post_a(req, API_URL = window.location.href, callback = null, preloader_place = null) {
    document.getElementById('preloader').classList.toggle('d-none')
    axios.post(API_URL, req)
        .then(function (response) {
            if (callback !== null) {
                callback(response);
            } else {
                return response;
            }
        })
        .catch(function (response, error) {
            console.log(error);
            return response;
        }).then(function (res) {
        document.getElementById('preloader').classList.toggle('d-none')
    })
}

function put_a(req, API_URL = window.location.href, callback = null, preloader_place = null) {
    document.getElementById('preloader').classList.toggle('d-none')
    axios.put(API_URL, req)
        .then(function (response) {
            if (callback !== null) {
                callback(response);
            } else {
                return response;
            }
        })
        .catch(function (response, error) {
            console.log(error);
            return response;
        }).then(function (res) {
        document.getElementById('preloader').classList.toggle('d-none')
    })
}

function get_a(req, API_URL = window.location.href, callback = null, preloader_place = null) {
    document.getElementById('preloader').classList.toggle('d-none')
    axios.get(API_URL, {
        params: req
    })
        .then(function (response) {
            if (callback) {
                callback(response);
            } else {
                return response;
            }
        }).then(function () {

    })
        .catch(function (response, error) {
            console.log(error);
            {
                console.log(error);
                return response;
            }
        }).then(function (res) {
        document.getElementById('preloader').classList.toggle('d-none')
    })
}