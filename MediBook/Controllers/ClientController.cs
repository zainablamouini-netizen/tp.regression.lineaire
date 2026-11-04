using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using MediBook.Data;
using MediBook.Models;

namespace MediBook.Controllers;

public class ClientController(MediBookContext context) : Controller
{
    public async Task<IActionResult> Index()
    {
        var clients = await context.Clients
            .OrderBy(client => client.LastName)
            .ThenBy(client => client.FirstName)
            .ToListAsync();

        return View(clients);
    }

    public async Task<IActionResult> Details(int? id)
    {
        if (id is null)
        {
            return NotFound();
        }

        var client = await context.Clients.FindAsync(id);
        return client is null ? NotFound() : View(client);
    }

    public IActionResult Create()
    {
        return View();
    }

    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create([Bind("FirstName,LastName,Email,Phone")] Client client)
    {
        if (!ModelState.IsValid)
        {
            return View(client);
        }

        context.Add(client);
        await context.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }

    public async Task<IActionResult> Edit(int? id)
    {
        if (id is null)
        {
            return NotFound();
        }

        var client = await context.Clients.FindAsync(id);
        return client is null ? NotFound() : View(client);
    }

    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Edit(int id, [Bind("Id,FirstName,LastName,Email,Phone")] Client client)
    {
        if (id != client.Id)
        {
            return BadRequest();
        }

        if (!ModelState.IsValid)
        {
            return View(client);
        }

        var existingClient = await context.Clients.FindAsync(id);
        if (existingClient is null)
        {
            return NotFound();
        }

        existingClient.FirstName = client.FirstName;
        existingClient.LastName = client.LastName;
        existingClient.Email = client.Email;
        existingClient.Phone = client.Phone;

        await context.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }

    public async Task<IActionResult> Delete(int? id)
    {
        if (id is null)
        {
            return NotFound();
        }

        var client = await context.Clients.FindAsync(id);
        return client is null ? NotFound() : View(client);
    }

    [HttpPost, ActionName("Delete")]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> DeleteConfirmed(int id)
    {
        var client = await context.Clients.FindAsync(id);
        if (client is null)
        {
            return NotFound();
        }

        context.Clients.Remove(client);
        await context.SaveChangesAsync();
        return RedirectToAction(nameof(Index));
    }
}
