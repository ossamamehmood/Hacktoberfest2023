const navbar = () => {
  return `
       <nav>
          <div id="nav-left-option">
            <div class="nav-Favorites-icon">
              <a href="">
                <div>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-heart"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"
                    />
                  </svg>
                </div>
                <div>Favorites</div></a
              >
            </div>
    
            <div class="nav-login-btn">
              <button type="button" class="btn" id="login-btn"><span id="login-span">Log in</span></button>
            </div>
    
            <div class="dropdown">
              <a
                class="btn btn-secondary dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
                id="nav-menuBTN"
              >
                Menu
              </a>
              <ul class="dropdown-menu" id="dropdown-menu-id">
                <li><a class="dropdown-item" href="#">Recently viewed</a></li>
                <li><a class="dropdown-item" href="#">Help and Support</a></li>
              </ul>
            </div>
    
            <div class="nav-INR">
              <select class="form-select" aria-label="Default select example">
                <option selected>INR</option>
                <option value="1">EUR-Euro</option>
                <option value="2">GBP-British</option>
                <option value="3">USD-US Dollar</option>
                <option value="4">AED</option>
                <option value="3">ARS</option>
                <option value="4">AUD</option>
                <option value="5">AZN</option>
                <option value="6">BGN</option>
                <option value="7">BHD</option>
                <option value="8">BRL</option>
                <option value="9">CAD</option>
                <option value="10">CHF</option>
                <option value="11">CLP</option>
                <option value="12">CNY</option>
                <option value="5">AZN</option>
                <option value="6">BGN</option>
                <option value="7">BHD</option>
                <option value="8">BRL</option>
                <option value="9">CAD</option>
                <option value="10">CHF</option>
                <option value="11">CLP</option>
                <option value="12">CNY</option>
              </select>
            </div>
          </div>
          <!-- </div> -->
        </nav>
    
        <div id="nav-Bar-2">
          <div id="nav-Deals-from">
            <div class="nav-Img-logo">
              <a href="index.html">
                <img
                  src="https://lh3.googleusercontent.com/p/AF1QipMA1spBSQdAHAfrhUfcZajJflHbGi_Xq_n936vz=w1080-h608-p-no-v0"
                  alt="trivago logo"
                />
              </a>
            </div>
    
            <div id="nav-text-Deals-from">
              <div><b><span id="detail-span">Deals from your favorite bookings sites</span></b></div>
              <div>
                <p>
                  Try searching for a city, a specific hotel, or even a landmark!
                </p>
              </div>
            </div>
          </div>
    
          <div id="nav-bar-3">
          <div id="nav-btn-house-Apartment">
            <button>All stays</button>
            <button>Hotel</button>
            <button>House / Apartment</button>
          </div>
    
          <div id="nav-input-main">
            <div id="nav-input-main-1">
              <div>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-search"
                  viewBox="0 0 16 16"
                  id="searchLogo"
                >
                  <path
                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
                  />
                </svg>
              </div>
              <div><input id="Mumbai-input" type="text" placeholder="Mumbai"/></div>
              <div>
                <button id="Mumbai-btn">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-x-lg"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"
                    />
                  </svg>
                </button>
              </div>
            </div>
    
            <div class="nav-input-main-2">
              <div>
                <div>Check in</div>
                <div><input type="date" id="check-in-date"/></div>
              </div>
              <div>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-chevron-left"
                  viewBox="0 0 16 16"
                >
                  <path
                    fill-rule="evenodd"
                    d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"
                  />
                </svg>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-chevron-right"
                  viewBox="0 0 16 16"
                >
                  <path
                    fill-rule="evenodd"
                    d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"
                  />
                </svg>
              </div>
            </div>
    
            <div class="nav-input-main-2">
              <div>
                <div>Check out</div>
                <div><input type="date" id="check-out-date"/></div>
              </div>
              <div>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-chevron-left"
                  viewBox="0 0 16 16"
                >
                  <path
                    fill-rule="evenodd"
                    d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"
                  />
                </svg>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-chevron-right"
                  viewBox="0 0 16 16"
                >
                  <path
                    fill-rule="evenodd"
                    d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"
                  />
                </svg>
              </div>
            </div>
    
            <div class="nav-input-main-2">
              <div id="nav-input-logo">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 16 16"
                  width="16"
                  height="16"
                >
                  <path
                    d="M2 5.5a3.5 3.5 0 1 1 5.898 2.549 5.508 5.508 0 0 1 3.034 4.084.75.75 0 1 1-1.482.235 4 4 0 0 0-7.9 0 .75.75 0 0 1-1.482-.236A5.507 5.507 0 0 1 3.102 8.05 3.493 3.493 0 0 1 2 5.5ZM11 4a3.001 3.001 0 0 1 2.22 5.018 5.01 5.01 0 0 1 2.56 3.012.749.749 0 0 1-.885.954.752.752 0 0 1-.549-.514 3.507 3.507 0 0 0-2.522-2.372.75.75 0 0 1-.574-.73v-.352a.75.75 0 0 1 .416-.672A1.5 1.5 0 0 0 11 5.5.75.75 0 0 1 11 4Zm-5.5-.5a2 2 0 1 0-.001 3.999A2 2 0 0 0 5.5 3.5Z"
                  ></path>
                </svg>
              </div>
              <div>
                <div>1 Room</div>
                <div>2 Guest</div>
              </div>
            </div>
    
            <div id="nav-input-main-5">
              <button type="button" id="searchButton5">Search</button>
            </div>
          </div>
    
          <div id="nav-We-compare">
            <b>We compare multiple booking sites at once</b>
          </div>
    
          <div id="nav-trip-oyo-booking">
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/395.png"
              alt="agoda"
            />
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/452.png"
              alt="host"
            />
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/626.png"
              alt="booking"
            />
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/2192.png"
              alt="makemy"
            />
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/14.png"
              alt="etc"
            />
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/634.png"
              alt="trip"
            />
            <img
              src="https://imgcy.trivago.com/image/upload/hardcodedimages/mpm-localised-logos-dark/2452.png"
              alt="oyo"
            />
            <p>+100 more</p>
          </div>
        </div>
        </div>
    `;
};

export default navbar;
