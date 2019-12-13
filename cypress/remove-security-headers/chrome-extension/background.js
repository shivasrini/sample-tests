const headersToRemove = [
  "x-frame-options",
  "content-security-policy"
]

const filter = {
  "urls": [
    "http://*/*",
    "https://*/*"
  ]
}

const opt_extraInfoSpec = [
  "responseHeaders", // Make sure the details object in the callback contains the responseHeaders object
  "blocking" // Make the callback function be synchronous
]

const callback = (details) => {
  // Filter out specific headers
  const responseHeaders = details.responseHeaders.filter(
    header => headersToRemove.indexOf(header.name.toLowerCase()) < 0
  )
  return {
    responseHeaders
  }
}

// Refer to https://developer.chrome.com/extensions/webRequest
// Especially the part titled "Registering Event Listeners"
chrome.webRequest.onHeadersReceived.addListener(callback, filter, opt_extraInfoSpec)