/// <reference types="cypress" />

describe('Test invalid login', function () {
    it('Login fails with an error message', function () {
        cy.visit('https://auth0.com')
        cy.contains('h1','Never Compromise on Identity').should('exist')
        cy.contains('USE AUTH0 FOR FREE').as('signupButton').click().then(() => {
            cy.get('input[name="email"]').as('emailTextBox').should('be.visible').and('be.enabled')
            cy.get(`@emailTextBox`).type('x@x.com')
            cy.get('input[name="password"]').as('passwordTextBox').should('be.visible').and('be.enabled')
            cy.get(`@passwordTextBox`).type('#####')
            cy.contains('SIGN UP').as('signupButton').click().then(() => {
                cy.get('.text-error-utils').should('have.text','The user already exists.')
            })
        })
    })
})