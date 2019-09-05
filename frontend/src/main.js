import Vue from 'vue'
import App from './App'
import Axios from 'axios'
import router from './router/index'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);
Vue.prototype.$http = Axios
Vue.prototype.FLASK_URL = 'http://127.0.0.1:8888'
Vue.config.productionTip = false



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  render: h => h(App),
  template: '<App/>'
})