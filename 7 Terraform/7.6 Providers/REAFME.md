# 1.

DataSource

https://github.com/hashicorp/terraform-provider-aws/blob/main/internal/provider/provider.go#L338

Resources

https://github.com/hashicorp/terraform-provider-aws/blob/main/internal/provider/provider.go#L709

name конфликтует с name_prefix

```text

"name": {
			Type:          schema.TypeString,
			Optional:      true,
			Computed:      true,
			ForceNew:      true,
			ConflictsWith: []string{"name_prefix"},
		},

"name_prefix": {
			Type:          schema.TypeString,
			Optional:      true,
			Computed:      true,
			ForceNew:      true,
			ConflictsWith: []string{"name"},
		},
```
Судя по коду ниже: 80 или 75 символов и Только малые и прописные латинские буквы, цифры, _ и - 

```text
	if fifoQueue {
			name = create.NameWithSuffix(diff.Get("name").(string), diff.Get("name_prefix").(string), FIFOQueueNameSuffix)
		} else {
			name = create.Name(diff.Get("name").(string), diff.Get("name_prefix").(string))
		}

		var re *regexp.Regexp

		if fifoQueue {
			re = regexp.MustCompile(`^[a-zA-Z0-9_-]{1,75}\.fifo$`)
		} else {
			re = regexp.MustCompile(`^[a-zA-Z0-9_-]{1,80}$`)
		}
		
		if !re.MatchString(name) {
			return fmt.Errorf("invalid queue name: %s", name)
		}
```
