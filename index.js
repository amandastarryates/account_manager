 function deleteAccount(accountId) {
    console.log("Deleting account " + accountId);
    fetch('/delete-account', {
        method: "POST",
        body: JSON.stringify({ accountId: accountId }),
        }).then((_res) => {
            window.location.href = "/";
    });
 }
