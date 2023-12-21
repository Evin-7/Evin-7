<template>
  <div>
    <vue-element-loading
      :active="appLoading"
      :is-full-screen="true"
      background-color="#FFFFFF"
      color="red"
      spinner="bar-fade-scale"
    />
    <v-snackbar v-model="snackbar" color="#3EA56E" right :timeout="timeout">
      <v-layout wrap>
        <v-flex text-left class="align-self-center">{{ msg }}</v-flex>
        <v-flex text-right>
          <v-btn small :ripple="false" text @click="snackbar = false">
            <v-icon style="color: white">mdi-close</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
    </v-snackbar>

    <v-layout wrap align-center>
      <v-flex xs12>
       
      
        <!-- <v-snackbar
          v-model="showSnackBar"
          color="#7056b3"
          top
          shaped
          :timeout="timeout"
        >
          <v-layout wrap justify-center>
            <v-flex text-left class="align-self-center">
              <span style="color: white">
                {{ msg }}
              </span>
            </v-flex>
            <v-flex text-right>
              <v-btn small :ripple="false" text @click="showSnackBar = false">
                <v-icon style="color: white">mdi-close</v-icon>
              </v-btn>
            </v-flex>
          </v-layout>
        </v-snackbar> -->
        <v-img
          class="align-center"
          src="../../assets/Images/R3.jpg"
        height="100%"
        width="100%"
        >
          <v-layout wrap justify-center>
            <v-flex xs12 lg9 align-self-center>
              <v-layout wrap justify-center>
                <v-flex xs12 sm6 md6 px-2>
                  <v-card tile>
                    <v-layout wrap justify-center>
                      <v-flex xs12  px-8 py-6>
                        <v-layout wrap>
                          <v-flex xs12 text-center>
                            <span class="titlefont" style="font-size: 30px">
                              Get in Touch with us!
                            </span>
                          </v-flex>

                          <v-flex pt-8 xs12 text-left>
                            <v-layout wrap justify-center>
                              <v-flex xs12>
                                <v-form @submit.prevent="validateInput">
                                  <v-text-field
                                    color="#e31e24"
                                    placeholder=" Name"
                                    regular
                                    v-model="contact.name"
                                  >
                                  </v-text-field>
                                </v-form>
                              </v-flex>
                            </v-layout>
                            <v-layout wrap justify-center>
                              <v-flex xs12>
                                <v-form @submit.prevent="validateInput">
                                  <v-text-field
                                    color="#e31e24"
                                    placeholder="Email"
                                    regular
                                    v-model="contact.email"
                                  >
                                  </v-text-field>
                                </v-form>
                              </v-flex>
                            </v-layout>
                            <v-layout wrap justify-center>
                              <v-flex xs12>
                                <v-form @submit.prevent="validateInput">
                                  <v-text-field
                                    color="#e31e24"
                                    placeholder="Phone Number"
                                    regular
                                    v-model="contact.phno"
                                  >
                                  </v-text-field>
                                </v-form>
                              </v-flex>
                            </v-layout>
                            <v-layout wrap justify-center>
                              <!-- <v-flex xs12>
                                <v-form @submit.prevent="validateInput">
                                  <v-select
                                    color="#e31e24"
                                    :items="intrest"
                                    placeholder="Interested In"
                                    regular
                                    v-model="contact.intrest"
                                  >
                                  </v-select>
                                </v-form>
                              </v-flex> -->
                            </v-layout>
                            <v-layout wrap justify-center>
                              <v-flex xs12>
                                <v-textarea
                                  auto-grow
                                  regular
                                  placeholder="Message"
                                  color="#e31e24"
                                  rows="2"
                                  row-height="30"
                                  v-model="contact.Message"
                                ></v-textarea>
                              </v-flex>
                            </v-layout>
                          </v-flex>
                          <v-flex xs12 text-right pt-4 pb-3>
                            <v-btn
                              dark
                              color="#e31e24"
                              height="50px"
                              width="140px"
                              light
                              :ripple="false"
                              style="border-radius: 15px"
                              depressed
                              @click="add()"
                            >
                              Send <v-icon>mdi-arrow-right</v-icon>
                            </v-btn>
                          </v-flex>
                        </v-layout>
                      </v-flex>
                    </v-layout>
                  </v-card>
                </v-flex>
                <v-spacer></v-spacer>
                <v-flex xs12 pl-4 sm6 md4 align-self-center>
                  <v-card flat color="transparent">
                    <v-flex  xs12 align-self-center text-left py-9>
                      <span class="titlefont" style="font-size: 30px">
                        Contact Us
                      </span>
                    </v-flex>
                    <v-flex xs12 align-self-center text-left pb-6>
                      <v-img
                        src="../../assets/Images/loc.png"
                        width="30px"
                        height="30px"
                      ></v-img
                    >
                    
                    </v-flex>
                    <v-flex xs12 align-self-center text-left pb-6>
                      <span class="titlefont2" style="font-size: 20px">
                        Door No.17/137/58, Aranattukara,<br />
                        2nd Floor Leshore Business Park,<br />
                        Thrissur, Kerala . <br />
                      </span>
                    </v-flex>
                    <v-flex xs12 align-self-center text-left pb-6
                      >
                  
                  
                  
                    <v-img
                        src="../../assets/Images/chat.png"
                        width="30px"
                        height="30px"
                      ></v-img
                    >
                  
                  </v-flex>
                    <v-flex
                      xs12
                      align-self-center
                      text-left
                      pb-6
                      style="text-align: justify"
                    >
                      <span class="titlefont2" style="font-size: 20px">
                        We create technology for you, and we’d love to hear from you.
                        Shoot a mail to us with an idea, a collaboration pitch
                        and be a harbinger of change. <br />
                      </span>
                    </v-flex>

                
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-img>
      </v-flex>
    </v-layout>
  </div>
</template>


<script>
import axios from "axios";
export default {
  data() {
    return {
      msg: "",


      timeout: 5000,
      
      snackbar: false,
      appLoading: false,
      contact: {
        name: null,
        email: null,
        phno: null,
      
        message: null,
      },
      // rules: {
      //   required: (value) => !!value || "Required.",
      //   counter: (value) => value.length <= 20 || "Max 20 characters",
      //   email: (value) => {
      //     const pattern =
      //       /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      //     return pattern.test(value) || "Invalid e-mail.";
      //   },
      // },
    };
  },
  methods: {
    add() {
     
      // if(this.$refs.form.validate())
      // {
      this.appLoading = true;
      axios({
        method: "POST",
        url: "/contactdetails",
        data: {
          fullName: this.contact.name,
          email: this.contact.email,
          phoneNumber: this.contact.phno,
          message: this.contact.Message,
        },
        // headers: {
        //   "x-auth-token": localStorage.getItem("token"),
        // },
      })
        .then((response) => {
          if (response.data.status) {
            this.msg = " message has been sent Successfully ";
            this.contact.phno=null;
            this.contact.email=null;
            this.contact.name=null;
            this.contact.Message=null;

            this.snackbar = true;

            this.appLoading = false;
            this.$refs.form.resetValidation();
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
 
  },
};
</script>