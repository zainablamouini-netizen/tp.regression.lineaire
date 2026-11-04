using MediBook.Models;
using Microsoft.EntityFrameworkCore;

namespace MediBook.Data;

public class MediBookContext(DbContextOptions<MediBookContext> options) : DbContext(options)
{
    public DbSet<Client> Clients => Set<Client>();
}
