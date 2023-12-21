<template>
  <div>
    <v-layout pl-lg-14 pl-xs-2 wrap fill-height>
      <v-snackbar v-model="snackbar" color="blue" right :timeout="timeout">
        <v-layout wrap>
          <v-flex text-left class="align-self-center">{{ msg }}</v-flex>
          <v-flex text-right>
            <v-btn small :ripple="false" text @click="snackbar = false">
              <v-icon style="color: white">mdi-close</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-snackbar>
      <v-flex xs12 lg8>
        <v-layout wrap>
          <v-flex
            pt-8
            pl-8
            pl-xs-3
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="300"
            xs12
            class="d-flex align-end mb-6 bg-surface-variant"
          >
            <span
              style="
                font-family: homefontsub2;
                color: #37aee5;
                text-align: justify;
              "
              :style="
                $vuetify.breakpoint.name == 'xs'
                  ? {
                      'font-size': '30px',
                    }
                  : $vuetify.breakpoint.name == 'sm'
                  ? {
                      'font-size': '20px',
                    }
                  : $vuetify.breakpoint.name == 'md'
                  ? {
                      'font-size': '25px',
                    }
                  : {
                      'font-size': '40px',
                    }
              "
              >Contact Us
            </span>
          </v-flex>
          <v-flex
            xs12
            pl-8
            pb-4
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="300"
            class="mainfont"
            style="font-size: 20px; font-weight: bold"
          >
            <span> {{ list.heading }} </span>
            <br />
            <br />
            <span v-html="list.msg" style="font-size: 17px; font-weight: bold">
             
            </span>
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex xs4 pt-6 text-right class="hidden-sm-and-down">
        <v-avatar tile size="110px">
          <v-img contain src="../assets/Images/cupattern1.png"></v-img>
        </v-avatar>
      </v-flex>
    </v-layout>
    <v-layout fill-height class="grad" wrap>
      <v-snackbar v-model="snackbar" color="blue" right :timeout="timeout">
        <v-layout wrap>
          <v-flex text-left class="align-self-center">{{ msg }}</v-flex>
          <v-flex text-right>
            <v-btn small :ripple="false" text @click="snackbar = false">
              <v-icon style="color: white">mdi-close</v-icon>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-snackbar>
      <vue-element-loading
        indeterminate
        :active="appLoading"
        :is-full-screen="true"
        background-color="#FFFFFF"
        color="#87ceeb"
        spinner="bar-fade-scale"
      />
      <v-flex xs12 text-left pt-4>
        <v-layout wrap>
          <v-flex
            data-aos="zoom-in-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="1000"
          >
            <v-img
              :height="
                $vuetify.breakpoint.name == 'xs'
                  ? '160px'
                  : $vuetify.breakpoint.name == 'sm'
                  ? '300px'
                  : $vuetify.breakpoint.name == 'md'
                  ? '1000px'
                  : $vuetify.breakpoint.name == 'lg'
                  ? '300px'
                  : '300px'
              "
              :width="
                $vuetify.breakpoint.name == 'xs'
                  ? '960px'
                  : $vuetify.breakpoint.name == 'sm'
                  ? '1000px'
                  : $vuetify.breakpoint.name == 'md'
                  ? '1000px'
                  : $vuetify.breakpoint.name == 'lg'
                  ? '1800px'
                  : '2800px'
              "
              :src="mediaURLnew + list.image"
            >
            </v-img>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>

    <v-layout justify-end wrap fill-height>
      <v-flex xs12 pt-10 text-center>
        <span
          style="font-family: homefontsub2; color: #37aee5; text-align: justify"
          :style="
            $vuetify.breakpoint.name == 'xs'
              ? {
                  'font-size': '30px',
                }
              : $vuetify.breakpoint.name == 'sm'
              ? {
                  'font-size': '20px',
                }
              : $vuetify.breakpoint.name == 'md'
              ? {
                  'font-size': '25px',
                }
              : {
                  'font-size': '30px',
                }
          "
          >Find us here!</span
        >
      </v-flex>
      <v-flex xs2 pb-3 class="hidden-sm-and-down" text-left align-self-end>
        <v-avatar tile size="110px">
          <v-img contain src="../assets/Images/cupattern1.png"></v-img>
        </v-avatar>
      </v-flex>
      <v-flex
        data-aos="zoom-in-up"
        data-aos-duration="1500"
        data-aos-delay="500"
        xs12
        pa-3
        pa="-lg-0"
        lg8
        text-center
      >
        <div id="map"></div>
      </v-flex>
      <v-flex xs2 text-right class="hidden-sm-and-down">
        <span>
          <v-avatar tile size="110px">
            <v-img
              contain
              src="../assets/Images/cupattern2png.png"
            ></v-img> </v-avatar
        ></span>
      </v-flex>
    </v-layout>
    <v-layout wrap justify-center>
      <v-flex text-center lg9 pa-3 pa-lg-14>
        <strong>
          <span class="mainfont"
            >{{ list.additionalContent }}</span
          ></strong
        >
      </v-flex>
    </v-layout>

    <v-layout wrap justify-center>
      <v-flex
        xs12
        lg10
        style="box-shadow: 0px 0px 100px rgba(0, 0, 0, 0.07)!important;"
      >
        <v-layout wrap justify-center>
          <v-flex
            xs12
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="500"
            lg7
            pl-2
            text-right
            class="mainfont"
            style="font-weight: bold"
          >
            <v-card
              color="white"
              class="card-shadow pl-6 pb-4 pr-14"
              elevation="0"
            >
              <v-layout wrap>
                <v-flex xs12 pt-10 pl-3 text-left>
                  <span
                    >Tell us a bit about yourself, and we’ll get in touch as
                    soon as we can</span
                  >
                </v-flex>
                <v-flex xs6 pl-4 pr-4 pt-10 text-left>
                  <span>Name</span>
                  <v-text-field
                    color="blue"
                    placeholder="Enter Name"
                    regular
                    v-model="contact.name"
                  >
                  </v-text-field>
                </v-flex>
                <v-flex xs6 pt-10 text-left>
                  <span>Location</span>

                  <v-text-field
                    color="blue"
                    placeholder="Location"
                    regular
                    type="text"
                    v-model="contact.location"
                  >
                  </v-text-field>
                </v-flex>
                <v-flex xs6 pl-4 pr-4 pt-10 text-left>
                  <span>Phone Number</span>
                  <v-text-field
                    color="blue"
                    placeholder="Enter Phone "
                    regular
                    type="number"
                    :rules="phnoRules"
                    v-model="contact.phoneNo"
                  >
                  </v-text-field>
                </v-flex>
                <v-flex xs6 pt-10 text-left>
                  <span>E-mail</span>
                  <v-text-field
                    color="blue"
                    :rules="emailRules"
                    placeholder="Enter Email"
                    regular
                    v-model="contact.email"
                  >
                  </v-text-field>
                </v-flex>
                <v-flex xs12 pa-3 text-left>
                  <span>Message</span>
                  <v-textarea
                    auto-grow
                    regular
                    placeholder="Message"
                    color="blue"
                    rows="2"
                    v-model="contact.msg"
                    row-height="30"
                  ></v-textarea>
                </v-flex>
                <v-flex xs12 text-right pb-3>
                  <v-btn
                    dark
                    color="blue"
                    height="30px"
                    width="140px"
                    light
                    class="zoom-card"
                    :ripple="false"
                    depressed
                    @click="validateInput()"
                  >
                    <span style="font-color: white"> SUBMIT</span>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-card>
          </v-flex>
          <v-flex
            xs12
            data-aos="slide-up"
            data-aos-ease="ease"
            data-aos-duration="1500"
            data-aos-delay="500"
            lg5
            style="background-color: #007cb6"
          >
            <v-layout wrap justify-end fill-height>
              <v-flex xs7 align-self-center>
                <v-layout class="mainfont" style="color: white" wrap>
                  <v-flex xs12 py-1>
                    <span style="
                font-family: mainfont;
                color: white;
                font-size: 20px;
               
              ">Contact Information</span>
                  </v-flex>
                  <v-flex xs12 py-1>
                    <v-layout wrap>
                      <v-flex xs2 pt-13>
                        <v-avatar size="30px" tile>
                          <v-img
                            contain
                            src="../assets/Images/cuicon1.png"
                          ></v-img>
                        </v-avatar>
                      </v-flex>
                      <v-flex xs10 pt-13 pl-4>
                        <span>{{ list.phoneNo }}</span>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12 py-1>
                    <v-layout wrap>
                      <v-flex xs2 pt-13>
                        <v-avatar size="30px" tile>
                          <v-img
                            contain
                            src="../assets/Images/cuicon5.png"
                          ></v-img>
                        </v-avatar>
                      </v-flex>
                      <v-flex xs10 pt-13 pl-4>
                        <span>{{ list.email }}</span>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                  <v-flex xs12 py-2>
                    <v-layout>
                      <v-flex xs2 pt-13>
                        <v-avatar size="30px" tile>
                          <v-img
                            contain
                            src="../assets/Images/cuicon6.png"
                          ></v-img>
                        </v-avatar>
                      </v-flex>
                      <v-flex xs10 pt-13 pl-4>
                        <span>{{ list.address }}</span>
                      </v-flex>
                    </v-layout>
                  </v-flex>
                </v-layout>
              </v-flex>
              <v-flex xs3 align-self-center>
                <v-img contain src="../assets/Images/cupattern3.png"></v-img>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>

    <v-layout wrap>
      <v-flex xs12 class="hidden-sm-and-down" text-right>
        <v-avatar tile size="110px">
          <v-img
            contain
            src="../assets/Images/cupattern1.png"
          ></v-img> </v-avatar
      ></v-flex>
    </v-layout>
  </div>
</template>
<script src="https://maps.googleapis.com/maps/api/js?libraries=places&key=AIzaSyBpukNl1L1qGqEwad87A1-MkZj8H_bKDZM&libraries=visualization,drawing"></script>

<script>
import axios from "axios";
var marker;
export default {
  data() {
    return {
      msg: "",
      list: {},
      timeout: 5000,
      snackbar: false,
      appLoading: false,
      latt: null,
      lonn: null,
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
      roleRules: [(v) => !!v || "Role is required"],
      phnoRules: [
        (v) => !!v || "phone is required",
        (v) => (v && v.length <= 10) || "invalid number",
        (v) => (v && v.length >= 10) || "invalid number",
        (v) => /^\d{10}$/.test(v) || "phone number must be a number",
      ],

      contact: {
        name: null,
        location: null,
        email: null,
        phoneNo: null,
        msg: null,
      },
      map: "",
      mapData: {},
    };
  },
  mounted() {
    this.detailsView();
    // if(this.list.locaion)
    // {
    // this.initMap();
    // }
  },
  methods: {
    add() {
      this.appLoading = true;
      axios({
        method: "POST",
        headers: {
          siteId: "6436362a65dc48eef99acd34",
        },
        url: "/user/add/enquiry",
        data: {
          name: this.contact.name,
          email: this.contact.email,
          phoneNo: this.contact.phoneNo,
          msg: this.contact.msg,
          location: this.contact.location,
        },
      })
        .then((response) => {
          if (response.data.status) {
            this.msg = " message has been sent Successfully ";
            this.contact.phoneNo = null;
            this.contact.email = null;
            this.contact.name = null;
            this.contact.msg = null;
            this.contact.location = null;
            this.snackbar = true;
            this.appLoading = false;
            location.reload();
          } else {
            this.msg = response.data.msg;
            this.snackbar = true;
          }
        })
        .catch((err) => {
          this.appLoading = false;

          console.log(err);
        });
    },
    detailsView() {
      this.appLoading = true;
      axios({
        method: "GET",
        headers: {
          siteId: "6436362a65dc48eef99acd34",
        },
        url: "/user/countactus/view",
      })
        .then((response) => {
          //  this.$router.go();
          this.list = response.data.data;
          this.latt = response.data.data.location[1];
          this.lonn = response.data.data.location[0];
          this.appLoading = false;
          this.initMap();
        })
        .catch((err) => {
          this.ServerError = true;
          console.log(err);
        });
    },

    validateInput() {
      if (!this.contact.name) {
        this.msg = "Please Provide name";
        this.snackbar = true;
        return;
      } else if (!this.contact.location) {
        this.msg = "Please Provide location";
        this.snackbar = true;
        return;
      } else if (!this.contact.phoneNo) {
        this.msg = "Please Provide phone number";
        this.snackbar = true;
        return;
      } else if (!this.contact.email) {
        this.msg = "Please Provide email";
        this.snackbar = true;
        return;
      } else if (!this.contact.msg) {
        this.msg = "Please Provide message";
        this.snackbar = true;
        return;
      } else {
        this.add();
      }
    },
    initMap() {
      var vm = this;
      var mapCanvas = document.getElementById("map");
      var mapOptions = {
        center: new google.maps.LatLng(this.latt, this.lonn),
        zoom: 10,

        mapTypeId: google.maps.MapTypeId.TERRAIN,
      };
      vm.map = new google.maps.Map(mapCanvas, mapOptions);
      var lat = this.latt;
      var lon = this.lonn;
      var latlngset = new google.maps.LatLng(lat, lon);

      marker = new google.maps.Marker({
        map: vm.map,
        position: latlngset,
      });
    },
  },
};
</script>
  <style scoped>
#map {
  height: 400px;
}
.test {
  text-align: justify;
}
.grad {
  background-image: linear-gradient(to right, #fbfbfb, #fbfbfb);
}

body {
  font-family: "Lato", sans-serif;
  background: #353535;
  color: #fff;
}
.jumbotron h1 {
  color: #353535;
}
footer {
  margin-bottom: 0 !important;
  margin-top: 80px;
}
footer p {
  margin: 0;
  padding: 0;
}
span.icon {
  margin: 0 5px;
  color: #d64541;
}
h2 {
  color: #bdc3c7;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.mrng-60-top {
  margin-top: 60px;
}
/* Global Button Styles */
a.animated-button:link,
a.animated-button:visited {
  position: relative;
  display: block;
  margin: 30px auto 0;
  padding: 14px 15px;
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  letter-spacing: 0.08em;
  border-radius: 0;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.2), 0 1px 0 rgba(0, 0, 0, 0.2);
  -webkit-transition: all 1s ease;
  -moz-transition: all 1s ease;
  -o-transition: all 1s ease;
  transition: all 1s ease;
}
a.animated-button:link:after,
a.animated-button:visited:after {
  content: "";
  position: absolute;
  height: 0%;
  left: 50%;
  top: 50%;
  width: 150%;
  z-index: -1;
  -webkit-transition: all 0.75s ease 0s;
  -moz-transition: all 0.75s ease 0s;
  -o-transition: all 0.75s ease 0s;
  transition: all 0.75s ease 0s;
}
a.animated-button:link:hover,
a.animated-button:visited:hover {
  color: #fff;
  text-shadow: none;
}
a.animated-button:link:hover:after,
a.animated-button:visited:hover:after {
  height: 450%;
}
a.animated-button:link,
a.animated-button:visited {
  position: relative;
  display: block;
  margin: 30px auto 0;
  padding: 14px 15px;
  color: #fff;
  font-size: 14px;
  border-radius: 0;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  letter-spacing: 0.08em;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.2), 0 1px 0 rgba(0, 0, 0, 0.2);
  -webkit-transition: all 1s ease;
  -moz-transition: all 1s ease;
  -o-transition: all 1s ease;
  transition: all 1s ease;
}

/* Victoria Buttons */

a.animated-button.victoria-three {
  border: 2px solid #d24d57;
}
a.animated-button.victoria-three:after {
  background: #d24d57;
  opacity: 0.5;
  -moz-transform: translateX(-50%) translateY(-50%);
  -ms-transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}
a.animated-button.victoria-three:hover:after {
  height: 140%;
  opacity: 1;
}
.card-shadow {
  box-shadow: 0px 2px 4px rgba(0, 0, red, 0.2);
}

.blur-radius-box-shadow {
  box-shadow: 5px 5px 20px;
}
</style>