import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';
import axios from 'axios';
import VueElementLoading from "vue-element-loading";
import AOS from 'aos';
import 'aos/dist/aos.css';

Vue.component("VueElementLoading", VueElementLoading);

Vue.config.productionTip = false;

// Set the base URL for Axios to your Flask backend's IP address
axios.defaults.baseURL = 'http://127.0.0.1:5000';

// Define the media URL for your backend
Vue.prototype.$mediaURL = 'http://127.0.0.1:5000/media/';

new Vue({
  vuetify,
  router,
  render: h => h(App),
  mounted() {
    AOS.init();
  },
}).$mount('#app');
