## Accounting API

This is a simple accounting REST API. Manage invoices, bills, expenses, acccounting books & reports.

- 🧾 **Invoices & Clients** - Generate detailed invoices for clients.
- 🔖 **Bills & Vendors** - Record bills received from vendors.
- 🛍 **Expenses** - Record all expenditures.
- 💸 **Payments** - Manage payments received on invoices & paymnets made on bills.
- 📦 **Inventory** - Simple stock tracking for items.
- 📖 **Double-Entry Accounting** - Automatic debit & credit entries for every transaction.
- 📊 **Journals & Reports** - Manage accounting books, record manual journals & generate accounting reports.
- 🏭 **Multiple Organsations** - Multi-tenancy architecture with semi-isolated approach using [PostgreSQL Schemas](https://www.postgresql.org/docs/current/ddl-schemas.html)

## Getting Started

First, clone the repo

```
git clone https://github.com/theedigerati/accounting-api.git && cd accounting-api
```

Next, run

```
docker compose up -d
```

The application will now be avalaible at <http://localhost:8000> and Swagger API docs at <http://localhost:8000/docs>

For  development, run

```
docker comoser up --watch
```
