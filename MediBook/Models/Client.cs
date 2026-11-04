using System.ComponentModel.DataAnnotations;

namespace MediBook.Models;

public class Client
{
    public int Id { get; set; }

    [Required]
    [StringLength(80)]
    [Display(Name = "Prénom")]
    public string FirstName { get; set; } = string.Empty;

    [Required]
    [StringLength(80)]
    [Display(Name = "Nom")]
    public string LastName { get; set; } = string.Empty;

    [Required]
    [EmailAddress]
    [StringLength(254)]
    [Display(Name = "Adresse e-mail")]
    public string Email { get; set; } = string.Empty;

    [StringLength(30)]
    [Display(Name = "Téléphone")]
    public string? Phone { get; set; }
}
