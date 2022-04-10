"use strict";

module.exports.createUser = (event, context, callback) => {
  console.log("PASSWORD_ITERATIONS: ", process.env.PASSWORD_ITERATIONS);
  console.log(
    "PASSWORD_DERIVED_KEY_LENGTH: ",
    process.env.PASSWORD_DERIVED_KEY_LENGTH
  );
  console.log("EMAIL_SERVICE_API_KEY: ", process.env.EMAIL_SERVICE_API_KEY);

  const response = {
    statusCode: 200,
    body: JSON.stringify({
      message: "User created",
    }),
  };

  callback(null, response);
};