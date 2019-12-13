/**
 * Tells Chrome to load an extension which will remove security headers from
 * external websites. Useful for remove iframe security headers from
 * the Doorman login screen
 * Refer to: https://github.com/cypress-io/cypress/issues/1763#issuecomment-394492373
 * @param {object} on - The cypress "on" object
 * @param {object} config - The cypress "config" object
 */
const removeSecurityHeadersFromExternalSites = (on, config) => {
  on("before:browser:launch", (browser = {}, args) => {
    if (browser.name === "chrome") {
      args.push(`--load-extension=${config.fileServerFolder}/node_modules/navex-cypress-utils/remove-security-headers/chrome-extension`)
    }
    return args
  })
}

module.exports = {
  removeSecurityHeadersFromExternalSites
}