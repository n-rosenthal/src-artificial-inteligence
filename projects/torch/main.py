from torch import device; from torch import nn;
from torch.utils.data import DataLoader;
from torchvision import datasets;
from torchvision.transforms import ToTensor

import torch;

def train(dataloader: DataLoader, model: nn.Module, loss_fn: nn.Module, optimizer: torch.optim.Optimizer) -> None:
    """
    Trains a model on the given data loader.

    Parameters:
        dataloader: The data loader containing the data to train the model on.
        model: The model to be trained.
        loss_fn: The loss function to use when computing the loss.
        optimizer: The optimizer to use when updating the model's parameters.
    """
    size = len(dataloader.dataset);
    model.train();
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(None), y.to(None, non_blocking=True)

        # Compute prediction error
        pred = model(X);
        loss = loss_fn(pred, y);

        # Backpropagation
        optimizer.zero_grad();
        loss.backward();
        optimizer.step();

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X);
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]");

def test(dataloader: DataLoader, model: nn.Module, loss_fn: nn.Module) -> None:
    """
    Tests a model on the given data loader.

    Parameters:
        dataloader: The data loader containing the data to test the model on.
        model: The model to be tested.
        loss_fn: The loss function to use when computing the loss.

    Prints the test error, including the accuracy and average loss.
    """
    size = len(dataloader.dataset);
    num_batches = len(dataloader);
    model.eval();
    test_loss, correct = 0, 0;
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device);
            pred = model(X);
            test_loss += loss_fn(pred, y).item();
            correct += (pred.argmax(1) == y).type(torch.float).sum().item();
    test_loss /= num_batches;
    correct /= size;
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n");
    

def main() -> None:
    device = "cuda" if torch.cuda.is_available() else "cpu";
    print(f"Using {device} device");

    # Download training data from open datasets.
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor(),
    );

    # Download test data from open datasets.
    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor(),
    );
    
    # Create data loaders.
    train_dataloader = DataLoader(training_data, batch_size=64);
    test_dataloader = DataLoader(test_data, batch_size=64);

    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(28*28, 512),
        nn.ReLU(),
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Linear(512, 10),
    ).to(device);

    loss_fn = nn.CrossEntropyLoss();
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-3);

    epochs = 1;
    for t in range(epochs):
        print(f"Epoch {t+1}\n-------------------------------");
        train(train_dataloader, model, loss_fn, optimizer);
        test(test_dataloader, model, loss_fn);
    print("Done!");

if __name__ == "__main__":
    main();